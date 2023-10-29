import datetime

# @classmethod : --> take class as the first argument as the class automatically

# @staticmethod : --> they dont pass the anything automatically like instance or class 

class Employee :

    def __init__(self , emp_name ,  cashWithdraw , cashDeposit):
        self.emp_name = emp_name
        self.cashWithdraw = cashWithdraw
        self.cashDeposit = cashDeposit

    # for classMethod : firstly you pass "Class" as the first argument
    @classmethod
    def set_bank_name(cls, bankName):
        cls.bank_name = bankName

    # since transaction time will be common to all instances
    # it will act as static method 
    # here static methods dont take any argument on their own. 
    # Generally  , functions which are independent of instance and class but you can access using instance or class . 
    @staticmethod
    def get_transaction_time():
        transactionTime = datetime.datetime.now()
        return transactionTime
    
    def get_current_bank_balance(self):
        return (self.cashDeposit - self.cashWithdraw)


if __name__ == "__main__":
    # emp1 = Employee("Sarthak", 1000 , 2000)
    # emp1.set_bank_name("PNB")
    # print(emp1.get_current_bank_balance())
    # print(emp1.get_transaction_time())
    # print("Bank Name of emp1 {0}".format(emp1.bank_name))
    # emp2 = Employee("Poorvaditya", 3000 , 5000)
    # emp1.set_bank_name("SBI")
    # print(emp1.get_current_bank_balance())
    # print(emp1.get_transaction_time())
    # print("Bank Name of emp2 {0}".format(emp2.bank_name))

    print(Employee.get_transaction_time()) # you can also access using class or instance