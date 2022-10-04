class shet:
    def __init__(self):
        self.balance = 0
        print ("аккаунт создан")
    
    def deposit(self):
        nach = float(input("введите сумму которую хотели бы внести = "))
        self.balance = nach + self.balance
        print("Сумма внесена и она составляет = " , self.balance)
    def withdraw(self):
        nach = float(input("введите сумму которую хотели бы снять = "))
        if(self.balance >= nach):
            self.balance = self.balance - nach
            print("баланс списан и составляет = ", self.balance )
        else:
            print("недостаточно баланса")


acc = shet()
acc.deposit()
acc.withdraw()