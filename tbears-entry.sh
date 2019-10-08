#!/bin/bash

service rabbitmq-server start

tbears start

echo ""
echo ""
echo "========================================="
echo "Deploying the SlotMachine contract"

TX=`tbears deploy slot-machine | grep -Eo "0x.*"`
echo "TX: $TX"

sleep 10

SCORE_ADDRESS=`tbears txresult $TX | grep -E '\"scoreAddress\"' | grep -Eo 'cx[0-9|a-z]*'`
echo "SCORE_ADDRESS: $SCORE_ADDRESS"

SEED_JSON="
{
  \"jsonrpc\": \"2.0\",
  \"method\": \"icx_sendTransaction\",
  \"params\": {
    \"version\": \"0x3\",
    \"from\": \"hxe7af5fcfd8dfc67530a01a0e403882687528dfcb\",
    \"value\": \"0xfffff05b59d3b200000000\",
    \"stepLimit\": \"0x200000\",
    \"nid\": \"0x3\",
    \"nonce\": \"0x2\",
    \"to\": \"$SCORE_ADDRESS\",
    \"dataType\": \"call\",
    \"data\": {
      \"method\": \"set_treasury\"
    }
  },
  \"id\": 1
}
"

echo $SEED_JSON
echo $SEED_JSON > seed.json

echo "========================================="
echo "Adding money to the treasury \n\n"
tbears sendtx seed.json

echo "========================================="
echo ""
echo ""
echo "Configure your application to use this CASINO_SCORE_ADDRESS address: $SCORE_ADDRESS"

exec /bin/bash