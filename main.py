class Account:
  def __init__(self,owner,balance=0.0):
    self.owner = owner
    self.balance = balance
  
  def __str__(self):
    return f"Account owner:\t\t{self.owner}\nAccount balance:\t{self.balance}"

  def withdraw(self,amount):
    if amount > self.balance:
        print("Funds Unavailable")
    else:
      self.balance -= amount
      print("Withdrawal Accepted")

  def deposit(self,amount):
    self.balance += amount
    print("Deposit Accepted")

acc = Account("Ryll",100)
print(acc)