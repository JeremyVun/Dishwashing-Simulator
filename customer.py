import random

# Event objects
# (1b)
class Customer:
  def __init__(self, name, wallet):
    self.name = name
    self.wallet = wallet

  def order(self):
    self.bill = random.randint(0, 100)
    print(f"{self.name} ordered ${self.bill}.00 worth of food!")

  def pay(self):
    amount_paid = min(self.wallet, self.bill)
    self.wallet -= amount_paid
    self.bill -= amount_paid

    print(f"{self.name} paid ${amount_paid:.2f} and owes ${self.bill:.2f}")


  # This represents the item when printed in a list
  def __repr__(self):
    return self.name