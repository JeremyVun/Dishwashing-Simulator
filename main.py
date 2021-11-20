from util.util import random_customer

from queue import Queue
from cashier import Cashier
from dishwasher import Dishwasher # (3) EXTENSION TASK

# Learn about queues and their practicel application in decoupled event management systems
def main():
  # (1a) - Queue datastructure
  cashier_queue = Queue()
  dishwashing_queue = Queue()

  # (1b) - Implement customer
  for i in range(10):
    cashier_queue.enqueue(random_customer())

  # (1c) - Implement first consumer/producer
  cashiers = [Cashier(i) for i in range(2)]

  # (3a) EXTENSION TASK - second consumer
  dishwashers = [Dishwasher(i) for i in range(1)]

  # (2a) - event loop
  round = 1
  while True:
    input(f"Round {round}. Press key to continue: ")

    # (2b) - Consume from queue
    print(f"\nCashier Queue: {cashier_queue}")
    for cashier in cashiers:
      cashier.serve_customer(cashier_queue, dishwashing_queue)

    # (3b) EXTENSION TASK - second consumer
    print(f"\nDishwashing Queue: {dishwashing_queue}")
    for dishwasher in dishwashers:
      dishwasher.wash_dishes(dishwashing_queue)

    round += 1

    print("")

main()