# ICON Blockchain Casino

This is the finished code for the ICON Blockchain Casino Localhost Workshop. 

Here is a guide to sharing ICX coins with the participants of your workshop. 

After the 'Create a Wallet' section of the workshop, you will disperse ICX coins between all of your participant's wallets. We've created a script to make this process as simple as possible. 

There are two steps:
* Gather everyone's wallet address and add them to a text file.
* Run a python script which sends each wallet an amount of test coins from our Test account. 

## Prework

You must be in a Morpheus Labs workspace to complete these steps. That is, run through the workshop slides using _this_ repositiory as your source code, instead of `mlh-localhost-blockchain-casino-starter` that your participants are using.  Complete the slides up until you have a Morpheus Labs workspace running.

## Step 1: Gather Wallet Addresses

At the point in the workshop where everyone has created a wallet, you need to gather the addresses. Do this whatever way is most convenient to you - a group chat, a shared spreadsheet, a chat client. 

Wallet addresses can be found in the ICON Chrome extension or app. They are a long string of random letters/numbers and begin with `hx`.

In your Morpheus Labs workspace, enter each wallet address on a new line in the file `webapp/participant_wallets.txt`.

For example, if you have 3 participants, your `participant_wallets.txt` file will look something like this:

```
hxac5688caf5a0c9742cffab2311d7b5728c569d10
hxbksak39599lkdlkcnqkdrlkhuqpuhsdlkjh11djf
hxnq3958ckdkjdhc94345ccff21dkjdhkjd39kqp1s
```
When you have all of your participants' wallet addresses, save the file. 

## Step 2: Share ICX Coins

Open a Terminal window (Terminal -> New Terminal) in your Morpheus Labs workspace. 

If you are not currently in the repository folder, change directory:

`cd mlh-localhost-icon-blockchain-casino`

Your Terminal line should look like this:

`root@workspace0ffbt5nuaj2bj6nu:/projects/mlh-localhost-icon-blockchain-casino#`

Install the required libraries and run the python script which will send ICX coins to each wallet:
```
pip3 install -r webapp/requirements.txt

python3 webapp/share_icx.py
```
The output of the successful script will look like the following:
```
Sharing ICX with Workshop Participants
======================================

Wallet Address: hxac5688caf5a0c9742cffab2311d7b5728c569d11
Transaction hash: 0x3282a60b36c4f571611e7e6031268fdb4ed2e5674364492b15be4cc18c3a17a8 

Wallet Address: hxac5688caf5a0c9742cffab2311d7b5728c569d12
Transaction hash: 0x9988f9c152bb49ffa744a0c4b616a636090e66fb349449c453c450d893c4fbaf 

Wallet Address: hxac5688caf5a0c9742cffab2311d7b5728c569d13
Transaction hash: 0x881b4653ea949c69fa38d57f1e009646f0b8afd647cc2643ea42125e949d4224 

All done!
```

## Debugging

If someone does not receive their ICX Coins, you can test the transaction to their wallet by running the following command in a Terminal window. Substitute the `0x` hash with the appropriate Transaction hash which was outputted from the `share_icx.py` script.

`tbears txresult 0x881b4653ea949c69fa38d57f1e009646f0b8afd647cc2643ea42125e949d4224`
This will output an error message if there is one. If the transaction was successful, double check that the wallet address is correct.


If you require the Wallet credentials:

* Wallet Address: `hxac5688caf5a0c9742cffab2311d7b5728c569d10`
* Wallet Password: `Mlh_icon_Bl0ckchain`

The Keystore file is found in this repository under `keystores/test_icx.json`.
