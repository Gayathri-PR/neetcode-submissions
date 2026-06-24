import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for n, c in freq.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for c, n in heap:
            res.append(n)
        return res
        