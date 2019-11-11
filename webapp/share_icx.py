import ast
import os
import sys

from iconsdk.builder.call_builder import CallBuilder
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.wallet.wallet import KeyWallet

import config

icon_service = IconService(HTTPProvider(config.ICON_SERVICE_PROVIDER_URL))

player_wallet = KeyWallet.load(
    config.PLAYER_WALLET_PRIVATE_KEY_FILE_PATH, config.PLAYER_WALLET_PASSWORD
)

# Create a new transaction and returns its hash
def create_transaction(wallet_address):
    transaction = (
        CallTransactionBuilder()
        .from_(player_wallet.get_address())
        .to(wallet_address)
        .method("play")
        .value(1032324764594)
        .step_limit(2000000)
        .nid(3)
        .nonce(100)
        .params({})
        .build()
    )

    signed_transaction = SignedTransaction(transaction, player_wallet)
    signed_transaction_hash = icon_service.send_transaction(signed_transaction)
    print('Transaction hash: {} '.format(signed_transaction_hash))
    return signed_transaction_hash

print('Sharing ICX with Workshop Participants')
print('======================================')

filepath = os.path.join(sys.path[0], 'participant_wallets.txt')
with open(filepath) as fp:
   line = fp.readline()
   while line:
       print("\nWallet Address: {}".format(line.strip()))
       current_wallet = line.strip()
       create_transaction(current_wallet)
       line = fp.readline()

print('\nAll done!')
