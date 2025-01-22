import heapq

class ProrityQueue:
    def __init__(self):
        self._queque = []
        self._index = 0

    def push(self, item, prority):
        heapq.heappush(self._queque, (-prority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queque)[-1]

