from bank_accounts import *

dave_acc = BankAccount(1000, 'Dave')
sarah_acc = BankAccount(2000, 'Sarah')

sarah_acc.transfer(2100, dave_acc)
dave_acc.deposit(1230)
dave_acc.withdrawal(2300)

sarah_accInt = InterestRewardsAcc(0,"Sarah")
sarah_accInt.deposit(25309)









































