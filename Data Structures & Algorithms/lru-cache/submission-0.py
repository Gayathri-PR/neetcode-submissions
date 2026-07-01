class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity        

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                # remove from current position and append to end as MRU
                t = self.cache.pop(i)
                self.cache.append(t)
                return t[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                t = self.cache.pop(i)
                # if exists, update the value and append to end as MRU
                t[1] = value
                self.cache.append(t)
                return
        # if length is same as capacity, pop the LRU
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        # add new value to list as MRU
        self.cache.append([key, value])
        
