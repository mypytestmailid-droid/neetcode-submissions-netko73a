# Neetcode 75 - Sort : DSA
# ===============================
# Python & SQL Sorting Cheat Sheet
# ===============================
#
# Python Sorting – Key Concepts & Interview Talking Points
#
# 1️⃣ list.sort() vs sorted()
# -----------------------------------
# • list.sort()
#   - Works only on lists
#   - Sorts in-place, modifies original list
#   - Returns None
#   - Syntax:
#         my_list.sort()                 # ascending
#         my_list.sort(reverse=True)     # descending
#         my_list.sort(key=len)          # custom key
#   - ✅ Interview Point: Mention it **modifies original list**.
#
# • sorted()
#   - Works on any iterable (list, tuple, dict, etc.)
#   - Returns a **new sorted list**
#   - Original data remains unchanged
#   - Syntax:
#         sorted(iterable)
#         sorted(iterable, reverse=True)
#         sorted(iterable, key=len)
#   - ✅ Interview Point: Useful when you need **original data intact**.
#
# 2️⃣ Sorting by Custom Keys
# -----------------------------------
# • Use 'key' for custom sorting logic:
#     sorted(lst, key=len)         # sort strings by length
#     sorted(lst, key=str.lower)   # case-insensitive sort
#     sorted(dict.items(), key=lambda x: x[1])  # sort dict by values
# • ✅ Interview Point: Always explain **why and what the key function does**.
#
# 3️⃣ Sorting Dictionaries
# -----------------------------------
# • By keys:
#     sorted(my_dict) or sorted(my_dict.keys())
# • By values:
#     sorted(my_dict.items(), key=lambda x: x[1])
# • Descending:
#     sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# • ✅ Interview Point: Demonstrates **Python versatility with dicts**.
#
# 4️⃣ Reverse Sorting
# -----------------------------------
# • Use reverse=True for descending order
# • Can combine with key for complex sorts
# • Example:
#     sorted(lst, key=len, reverse=True)
# • ✅ Interview Point: Shows **control over sorting order**.
#
# 5️⃣ Stability of Sort
# -----------------------------------
# • Python uses Timsort (stable sort)
# • Equal keys preserve original order
# • Example: Multi-level sorting
#     sorted(lst, key=lambda x: (x[1], x[0]))
# • ✅ Interview Point: Important in **multi-level sorting problems**.
#
# 6️⃣ Time Complexity
# -----------------------------------
# • Timsort: O(n log n) average, worst-case
# • ✅ Interview Point: Mention efficiency in **real-world data**.
#
# 7️⃣ Examples – Python
# -----------------------------------
# List sorting
# >>> lst = ["apple", "banana", "cherry"]
# >>> lst.sort()
# >>> lst
# ['apple', 'banana', 'cherry']
#
# Descending
# >>> sorted_lst = sorted(lst, reverse=True)
# >>> sorted_lst
# ['cherry', 'banana', 'apple']
#
# Dictionary sorting
# >>> d = {"apple": 3, "banana": 1, "cherry": 2}
# >>> sorted(d.items(), key=lambda x: x[1])  # by values
# [('banana', 1), ('cherry', 2), ('apple', 3)]
#
# 8️⃣ SQL Sorting – ORDER BY
# -----------------------------------
# • Used to sort query results
# • Syntax:
#     SELECT column1, column2
#     FROM table_name
#     ORDER BY column1 ASC;        -- ascending
#     ORDER BY column1 DESC;       -- descending
# • Multiple columns (multi-level sort):
#     SELECT * FROM employees
#     ORDER BY department ASC, salary DESC;
# • ✅ Interview Point: Connect Python sorting to SQL ORDER BY when discussing **data retrieval & ordering**.
#
# 9️⃣ Articulation Points for Interviews
# -----------------------------------
# • Always clarify whether **original data can be modified**.  
# • Mention **list.sort() modifies in place, sorted() returns new list**.  
# • Explain **key** usage clearly with examples.  
# • Show **stability** if asked about multi-level sorting.  
# • Discuss **time complexity**: Timsort O(n log n).  
# • Relate Python sorting to **SQL ORDER BY** for full-stack/data context.  

from typing import List

sort_list = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]
sort_list.sort()
print(sort_list)
def sort_words(words: List[str]) -> List[str]:
    return sorted(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    return sorted(numbers)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

sort_decimals_reverse = [3.14, 2.82, 6.433, 7.9, 21.555, 21.554]
print(sorted(sort_decimals_reverse, reverse=True))



