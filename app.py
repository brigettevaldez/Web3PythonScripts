from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/2ea1de64cd42468bbf72998ed16b74ae"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance('0x8b58D3EAcFC19fE81EE2866f27faFB9d9b978C91')
print(web3.fromWei(balance, "ether"))
