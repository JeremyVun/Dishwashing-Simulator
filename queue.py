# Learn how to create an ADT using more primitive types
# i.e. Queue from a list

# (1a)
class Queue:
  def __init__(self):
    self.__list = [] #__list to make this private

  # Queues do not allow nulls/nones
  def enqueue(self, person):
    if person != None:
      self.__list.append(person)
      
  def dequeue(self):
    if len(self.__list) != 0:
      return self.__list.pop(0)

  def __str__(self):
    return str(self.__list).replace(",", " -> ")
