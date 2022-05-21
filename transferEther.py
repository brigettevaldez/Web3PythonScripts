#
# Use ganache to transfer ether from one account to another
#

import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account_1 = "0x3aBa7A217673Fb0fddb4e53f933D6561139CD093"
account_2 = "0xF302eb18738aAb2ec851FAe00307F48a4Af99b60"
private_key = "3a13f4aabb59a01cbfd460fa262423dd650b4ee0f29d9f61cec8fc040f3cd291"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build transaction
tx = {
'nonce': nonce,
'to': account_2,
'value': web3.toWei(1, 'ether'),
'gas': 2000000,
'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))
