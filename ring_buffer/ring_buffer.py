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
        if len(self.data) == 4:
            self.data.appendleft(item)

    def get(self):
        # pass
        # print(self.data)
        for i in self.data:
            self.stack.append(i)
        return self.stack


