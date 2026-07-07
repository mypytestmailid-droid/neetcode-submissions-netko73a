class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #dedup step using set()
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1  not in num_set:
                length = 1 #this would be the start of the consecutive seq
                while num+length in num_set:# this identifies next consecutive num
                    length += 1
                longest = max(longest, length)
        return longest

obj = Solution()




        