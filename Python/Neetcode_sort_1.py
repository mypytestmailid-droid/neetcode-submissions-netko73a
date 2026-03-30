from typing import List


def sort_words(words: List[str]) -> List[str]:
    #return sorted(words,key=len,reverse=True)
    words.sort(key=len,reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    #return sorted(numbers,reverse=True)
    #numbers.sort(reverse=True) #The function was sorting the numbers based on their actual value (e.g., -19 comes before 1) rather than their absolute value.
    numbers.sort(key=abs, reverse=False) #added key=abs to the .sort() method in sort_numbers. This ensures that the numbers are compared based on their distance from zero (magnitude) rather than their signed value.
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))