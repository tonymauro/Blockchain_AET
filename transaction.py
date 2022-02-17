#import web3 and connect to localhost over HTTP
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

#get account data
accounts = w3.eth.accounts

#unlock personal account (first account), requires you to enter the account's password (which is password1 for me)
w3.geth.personal.unlockAccount(accounts[0],"password1",15000)

#prints accounts and balances
print(accounts)
print(w3.eth.get_balance(accounts[0]))
print(w3.eth.get_balance(accounts[1]))

#creates transaction
tx = {'from':accounts[0], 'to':accounts[1],'value':w3.toWei(0.5,"ether")}

#sends transaction and saves the hash
thash = w3.eth.send_transaction(tx)

#mine the transaction and stop mining when we receive a transaction receipt
w3.geth.miner.start(1)
w3.eth.wait_for_transaction_receipt(thash)
w3.geth.miner.stop()

#Print new account balances. Currently, mining a block gives you 2 ETH, so it looks like the balance of both accounts went up
print(w3.eth.get_balance(accounts[0]))
print(w3.eth.get_balance(accounts[1]))
