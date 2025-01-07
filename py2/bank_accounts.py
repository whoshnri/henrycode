class BankAccount:
    def __init__(self, initial , acc_name):

        self.balance = initial
        self.name = acc_name
        print(f'\nAccount for {self.name} created \nBalance : ${self.balance:.2f} ')

    def get_balance(self):
        print(f'\n{self.name}\'s balance is ${self.balance:.2f}')


    def deposit(self, amount):
        self.balance += amount
        print(f'\n{self.name}, your deposit of ${amount:.2f} was successful....✅✅\nNew balance is ${self.balance:.2f}')

    def withdrawal(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'\n{self.name}, your withdrawal of ${amount:.2f} was successful..✅✅\nNew balance is ${self.balance:.2f}')
        else :
            print(f'\n{self.name}, your withdrawal of ${amount:.2f} was unsuccessful due to insufficient funds.\nYour current balance is ${self.balance:.2f}')

    def transfer(self , amount , beneficiary):
        if self.balance >= amount :
            print('\n ************* \n')
            print('Beginning Transfer...🚀\n')
            if type(beneficiary) == BankAccount:
                if self.name == beneficiary.name:
                    print('\nTransfer Interrupted...🚫')
                    print('\nCannot transfer to yourself!\n***********')
                else :
                    self.balance -= amount
                    beneficiary.balance += amount
                    print(f'Your transfer of ${amount} to {beneficiary.name} was successful...✅✅\nNew balance is ${self.balance}\n***********')
                

            else:
                print('\n Please enter a valid account\n***********')
        else: 
            print('\n Insufficient funds to initaite transaction\n***********')
                
class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance += (1.05 * amount)
        print(f'\nDeposit of ${amount} complete. Interest of ${amount * 0.05:.2f} has been added successfully.')
        print(f'\nNew balance is ${self.balance:.2f}')   






