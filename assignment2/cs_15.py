# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class Customer:
    def __init__(self, f_name, l_name, m_name, id, phone, account_number, balance):
        self.f_name = f_name
        self.l_name = l_name
        self.m_name = m_name
        self.id = id
        self.account_number = account_number
        self.balance = balance

    def account_info(self):
        print("This is the account information")
        print("This account belongs to Mr./Mrs. {} {} {}. his account number is {}.".format(
            self.f_name, self.m_name, self.l_name, self.account_number))
        print("His registration id number is {}.".format(self.id))
        print("Total balance is Rs. {}".format(self.balance))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


c = Customer("Jidesh", "baidya", "Govinda", 2801,
             9860637891, 35230123414, 300000)
c.account_info()
