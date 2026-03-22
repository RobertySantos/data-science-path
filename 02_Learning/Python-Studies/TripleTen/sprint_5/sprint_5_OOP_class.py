from datetime import datetime

class Account:
    def __init__(self, bank, acc_id, holder_id, balance:float = 0.0):
        self.bank = bank
        self.acc_id = acc_id
        self.holder_id = holder_id
        self.balance = balance
        self.start_date = datetime.now()
    
    def deposit(self,amount:float):
        self.balance += amount
        
    
    def withdraw(self,amount:float):
        self.balance -= amount
        
    @staticmethod 
    def bankphone(bank):
        print('1-000-1234567')
     
    @classmethod   
    def quick(cls,string):
        acc_id, holder_id = string.split('/')
        return cls('default_bank', acc_id, holder_id,0.0)
    
    