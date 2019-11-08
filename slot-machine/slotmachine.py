from iconservice import *

TAG = "SLOT_MACHINE"
PAYOUT_MULTIPLIER = 10


class SlotMachine(IconScoreBase):
    _PLAY_RESULT = "PLAY_RESULT"

    @eventlog(indexed=1)
    def SlotMachine(self, _by: Address, amount: int, result: str):
        pass

    @eventlog(indexed=3)
    def FundTransfer(self, backer: Address, amount: int, is_contribution: bool):
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._play_results_array = ArrayDB(self._PLAY_RESULT, db, value_type=str)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external
    @payable
    def set_treasury(self) -> None:
        Logger.info(
            f"{self.msg.value} was added to the treasury from address {self.msg.sender}",
            TAG,
        )

    @external(readonly=True)
    def get_treasury(self) -> int:
        Logger.info(
            f"Amount in the treasury is {self.icx.get_balance(self.address)}", TAG
        )
        return self.icx.get_balance(self.address)

    @payable
    @external
    def play(self):
        amount = self.msg.value
        balance = self.icx.get_balance(self.address)
        Logger.info(f"Current Balance {balance}.", TAG)

        if balance <= amount * PAYOUT_MULTIPLIER:
            revert(f"Balance {balance} not enough to pay a prize.")

        if amount <= 0 or amount > 10 ** 24:
            revert(f"Betting amount {amount} out of range.")

        payout = min(amount * PAYOUT_MULTIPLIER, balance)

        win = False
        if balance % 10 == 0:
            win = True
    
        json_result = {
            "index": self.tx.index,
            "nonce": self.tx.nonce,
            "from": str(self.tx.origin),
            "timestamp": self.tx.timestamp,
            "txHash": bytes.hex(self.tx.hash),
            "amount": amount,
            "result": win,
        }

        self._play_results_array.put(str(json_result))

        # based on result pay the winner.
        if win:
            Logger.info(f"Amount owed to winner: {payout}", TAG)

            try:
                self.icx.transfer(self.msg.sender, payout)
                self.FundTransfer(self.msg.sender, payout, False)
                Logger.info(
                    f"Player won. Sent winner ({self.msg.sender}) {payout}.", TAG
                )
            except:
                Logger.info(f"Problem. Winnings not sent. Returning bet.", TAG)
                revert("Problem. Winnings not sent. Returning bet.")

        # else keep the amount in the treasury.
        else:
            Logger.info(f"Player lost. ICX retained in treasury.", TAG)

    @external(readonly=True)
    def get_results(self) -> dict:
        valueArray = []
        for value in self._play_results_array:
            valueArray.append(value)

        Logger.info(f"{self.msg.sender} is getting results", TAG)
        return {"result": valueArray}