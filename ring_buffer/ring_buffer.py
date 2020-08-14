class RingBuffer:
    def __init__(self, capacity):
        # pass
        from collections import deque
        self.capacity = capacity
        self.stack = []
        self.data = deque([], maxlen=capacity)

    def append(self, item):
        # pass
        self.data.append(item)
        if self.data.index == 3:
            self.data.appendleft(item)

    def get(self):
        # pass
        for i in self.data:
            self.stack.append(i)
        return self.stack


