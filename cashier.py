# First Event Consumer

# (1c)
class Cashier:
  def __init__(self, id):
    self.id = id

  def serve_customer(self, payment_queue, dishwashing_queue):
    customer = payment_queue.dequeue()

    if customer != None:
      print(f"\nCashier {self.id} serves {customer.name}")
      customer.order()
      customer.pay()

      if customer.bill == 0:
        print(f"Cashier {self.id} wishes {customer.name} a nice day")
      else:
        print(f"Cashier {self.id} puts {customer.name} onto the dishwashing queue")
        dishwashing_queue.enqueue(customer)
