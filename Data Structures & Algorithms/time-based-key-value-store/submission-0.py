import collections
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # get all values with timestamps for the key
        arr = self.store[key]
        l = 0
        r = len(arr) - 1
        ans = ""
        while l <= r:
            m = (l+r)//2
            if arr[m][0] <= timestamp:
                ans = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return ans
        
