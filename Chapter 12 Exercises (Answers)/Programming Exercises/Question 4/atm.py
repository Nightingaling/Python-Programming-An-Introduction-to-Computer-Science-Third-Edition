'''
What information the account has:
1. user ID
2. PIN
3. Balance in checking account
4. Balance in saving account

What can it do:
1. Check balance # Once user entered successfully UI will display balances
2. Withdraw cash # Need to update the UI once withdraw
3. Transfer money between accounts # Need to update UI once transfered
'''

class ATM:

    def __init__(self):
        infile = open("users.txt", 'r')
        self.user = {}
        for i in infile.readlines():
            ID = i.split(",")[0]
            pin = int(i.split(",")[1])
            self.user[ID] = pin
        infile.close()

    def checkID(self, identification):
        self.ID, pin = identification.getEntry()
        while True:
            if self.ID not in self.user:
                identification.fail()
            elif self.user[self.ID] != int(pin):
                identification.fail()
            else:
                identification.close()
                return True
            self.ID, pin = identification.getEntry()

    def getAccounts(self):
        infile = open("accounts.txt", 'r')
        self.accounts = {}
        for i in infile.readlines():
            accountID = i.split(",")[0]
            checking = float(i.split(",")[1])
            savings = float(i.split(",")[2])
            self.accounts[accountID] = [checking, savings]
        self.checking, self.savings = self.accounts[self.ID]
        infile.close()

    def run(self, interface):
        self.interface = interface
        self.getAccounts()
        choice = ''
        while choice != "quit":
            if choice == 'withdraw':
                self.withdraw()
            elif 'transfer' in choice:
                self.transfer(choice)
            elif choice == 'enquiry':
                self.interface.Enquiry(self.checking, self.savings)
            choice, self.amt = self.interface.servicesPressed()
        self.update()
        
    def withdraw(self):
        if self.amt < 10:
            self.interface.lessthan10Amount()
        elif self.amt > self.checking:
            self.interface.insufficentAmount()
        else:
            self.checking = self.checking - self.amt
            self.interface.successfulTransaction(self.amt)

    def transfer(self, choice):
        if self.amt < 10:
            self.interface.lessthan10Amount()
        if 'saving' in choice:
            if self.amt > self.savings:
                self.interface.insufficentAmount()
            else:
                self.savings = self.savings - self.amt
                self.checking = self.checking + self.amt
                self.interface.successfulTransaction(self.amt)
        elif 'checking' in choice:
            if self.amt > self.checking:
                self.interface.insufficentAmount()
            else:
                self.savings = self.savings + self.amt
                self.checking = self.checking - self.amt
                self.interface.successfulTransaction(self.amt)

    def update(self):
        self.accounts[self.ID] = self.checking, self.savings
        outfile = open("accounts.txt", 'w')
        for i in self.accounts:
            print('{0},{1},{2}'.format(i, self.accounts[i][0], self.accounts[i][1]), file=outfile)
        outfile.close()
