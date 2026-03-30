from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #step1: Create an empty set to keep track of numbers we've seen
        #Sets are ideal because checking for membership is O(1) on average
        seen = set()
        
        #Step2: Loop through each number in the input list/array
        for num in nums:
            #Step2a: Check if the current number is already in the 'Seen' set
            #If yes, it means this number has appeared before ->duplicate found.
            if num in seen:
                return True #Duplicate found, return True
            #Step2b: If the number is not in the set, add it
            #So we can check future numbers against this
            seen.add(num)
            
        #Step3: If the loop finishes without any duplicates found, return False
        return False
        
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4, 5]))  # False → no duplicates
print(sol.hasDuplicate([1, 2, 3, 2, 4, 5]))  # True → '2' is a duplicate
print(sol.hasDuplicate([1, 1, 1, 1]))        # True → '1' is duplicated multiple times
print(sol.hasDuplicate([]))                  # False → empty list has no duplicates