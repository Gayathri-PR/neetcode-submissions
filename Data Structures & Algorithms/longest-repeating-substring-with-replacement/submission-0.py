class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = 0
        longest = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            # if length of substring - maxFreq exceeds k, we need to make it eual to k for k replacements
            while (r-l+1) - maxFreq > k:
                count[s[l]]-= 1
                l+= 1
            longest = max(longest, r-l+1)
        return longest
        