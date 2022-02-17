from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
accounts = w3.eth.accounts
w3.geth.personal.unlockAccount(accounts[0],"password1",15000)
print(accounts)
print(w3.eth.get_balance(accounts[0]))
print(w3.eth.get_balance(accounts[1]))
tx = {'from':accounts[0], 'to':accounts[1],'value':w3.toWei(0.5,"ether")}
thash = w3.eth.send_transaction(tx)
w3.geth.miner.start(1)
w3.eth.wait_for_transaction_receipt(thash)
w3.geth.miner.stop()
print(w3.eth.get_balance(accounts[0]))
print(w3.eth.get_balance(accounts[1]))
