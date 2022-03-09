#Make sure that the user data for two accounts is in the correct format
def validate(lst):
	if (len(lst)!=2):
		return False
	for i in lst:
		if (not i.isnumeric()):
			return False
		elif (int(i)==0):
			return False
	return True

#User input for accounts
a1 = 0
a2 = 0
accountInput = ""
while (not validate(accountInput)):
	accountInput = input("Enter two accounts in the format '<from> <to>' to send a transaction between. Use account numbers that are above 0").split()
a1,a2 = map(int,accountInput)

#User input for transaction value
ethInput = ""
while (not ethInput.isnumeric())"
	ethInput = input("Enter the value of the transaction in ETH")
ethTransact = int(ethInput)

#import web3 and connect to localhost over HTTP
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

#get account data
accounts = w3.eth.accounts

#unlock personal account (first account), requires you to enter the account's password (which is password1 for me)
w3.geth.personal.unlockAccount(accounts[0],"password1",15000)

#prints accounts and balances
print(accounts)
print(w3.eth.get_balance(accounts[a0]))
print(w3.eth.get_balance(accounts[a1]))

#creates transaction
tx = {'from':accounts[a0], 'to':accounts[a1],'value':w3.toWei(ethTransact,"ether")}

#sends transaction and saves the hash
thash = w3.eth.send_transaction(tx)

#mine the transaction and stop mining when we receive a transaction receipt
w3.geth.miner.start(1)
w3.eth.wait_for_transaction_receipt(thash)
w3.geth.miner.stop()

#Print new account balances. Currently, mining a block gives you 2 ETH, so it looks like the balance of both accounts went up
print(w3.eth.get_balance(accounts[a1]))
print(w3.eth.get_balance(accounts[a2]))
