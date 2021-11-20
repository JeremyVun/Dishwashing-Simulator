# Part 3 - EXTENSION TASK - Second event consumer
class Dishwasher:
  def __init__(self, id):
    self.id = id

  def wash_dishes(self, dishwashing_queue):
    customer = dishwashing_queue.dequeue()

    if (customer == None):
      print(f"The pile of dishes grows larger at dishwasher {self.id}...")
    else:
      dishes_washed = int(customer.bill)

      print(f"{customer.name} scrubbed {dishes_washed} pots & pans at dishwasher {self.id}")
