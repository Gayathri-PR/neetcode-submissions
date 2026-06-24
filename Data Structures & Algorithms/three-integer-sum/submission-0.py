class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            # duplicate check
            if i > 0 and v == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = v + nums[l] + nums[r]
                if currSum > 0:
                    r-= 1
                elif currSum < 0:
                    l+= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l+= 1
                    r-= 1
                    # duplicate check
                    while l < r and nums[l] == nums[l-1]:
                        l+= 1
        return res
        