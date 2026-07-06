from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #to append similar words under same key as list
        for word in strs:
            key = tuple(sorted(word))
            result[(key)].append(word)
        return list(result.values())
obj = Solution()


        