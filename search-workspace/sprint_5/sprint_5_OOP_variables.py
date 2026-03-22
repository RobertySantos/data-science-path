from sprint_5_OOP_class import Account

first = Account('old_trusty','001','10043',500)
first.deposit(250)
first.withdraw(400)

print(first.balance)

second = Account.quick('002/10123')
print(second.start_date)