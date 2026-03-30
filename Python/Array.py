#finding duplicates in an array
from typing import List

class Solution:
    def hasDuplicates(self, nums: List[int]) -> bool:
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
print(sol.hasDuplicates([1, 2, 3, 4, 5]))  # False → no duplicates
print(sol.hasDuplicates([1, 2, 3, 2, 4, 5]))  # True → '2' is a duplicate
print(sol.hasDuplicates([1, 1, 1, 1]))        # True → '1' is duplicated multiple times
print(sol.hasDuplicates([]))                  # False → empty list has no duplicates
    
    
    
#from typing import List
#
#class Solution:
#    # Method to check if there is **any duplicate** (returns True/False)
#    def hasDuplicate(self, nums: List[int]) -> bool:
#        seen = set()  # To track numbers we've already seen
#        for num in nums:
#            if num in seen:
#                return True  # Duplicate found, return immediately
#            seen.add(num)
#        return False  # No duplicates found
#
#    # Method to **find all duplicates** in the list and return them
#    def allDuplicates(self, nums: List[int]) -> List[int]:
#        seen = set()        # Track numbers we've seen so far
#        duplicates = set()  # Track numbers that appear more than once
#        
#        for num in nums:
#            if num in seen:
#                # If number already seen, add it to duplicates set
#                duplicates.add(num)
#            else:
#                # If number not seen before, add to seen set
#                seen.add(num)
#        
#        # Convert set to list before returning
#        return list(duplicates)
#    
#sol = Solution()
#nums = [1, 2, 3, 2, 4, 3, 5]
#
#print(sol.hasDuplicate(nums))   # True → at least one duplicate exists
#print(sol.allDuplicates(nums))  # [2, 3] → all numbers appearing more than once