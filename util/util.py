# This helper code creates random customers

import json
import random
from customer import Customer

names = []

def load_names():
  global names
  with open('util/names.json', 'r') as f:
    names = json.load(f)["names"]

def random_customer():
  if len(names) == 0:
    load_names()

  name = names.pop(random.randint(0, len(names)-1))

  wallet = random.randint(0, 100)
  return Customer(name, wallet)
