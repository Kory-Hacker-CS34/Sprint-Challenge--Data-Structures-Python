class RingBuffer:
    def __init__(self, capacity):
        from collections import deque
        self.capacity = capacity
        self.current = 0
        self.data = [None]*self.capacity
        # self.data = deque([], maxlen=capacity)


    def append(self, item):
        self.data[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0
        # if len(self.data) == 4:
        #     self.data.insert(current, item)
        # print(self.data)

    def get(self):
        return self.data