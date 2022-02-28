# Python script to send a transaction

This script sends a transaction between two accounts on Geth. <br> <br><br>

## Important

Accounts to send transaction between must be specified in line 13-14, 17, 28-29. Blockchain must be unlocked on line 9 with the coinbase account and password

## Explanation
- Line 1 imports the Web3 library <br>
- Line 2 connects to localhost, which has Geth running, over HTTP (Port 8545) <br>
- Line 6 gets account data <br>
- Line 9 unlocks the coinbase account to allow mining <br>
- Lines 12-14 print the accounts and the balances of the accounts in the transaction <br>
- Line 17 creates the transaction between certain accounts and for a certain amount of ETH <br>
- Line 20 sends the transaction and saves the transaction hash <br>
- Line 23 begins mining <br>
- Line 24 waits for a transaction receipt. The program stops executing any code until it confirms the transaction has been sent, which occurs when the first block is mined successfully and the transaction is saved in the chain <br>
- Line 25 stops the miner <br>
- Lines 28-29 print the new account balance of the accounts involved in the transaction

## Further Development
- Automate the script/allow user input
- Don't use insecure unlock to unlock mining - figure out another way
- Do not mine with the same account that is involved in a transaction
