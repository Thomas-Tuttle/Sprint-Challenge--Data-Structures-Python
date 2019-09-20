class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item): 
    self.storage[self.current] = item         # Stores the current input item
    if self.current + 1 > self.capacity - 1:   # If the current set of items is more than the
        self.current = 0                       # capacity replace current, if not add it.
    else:
        self.current += 1

  def get(self):
    return [value for value in self.storage if value is not None] # returns a value if its there