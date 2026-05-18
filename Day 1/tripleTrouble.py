# Triple Trouble 
#       Given an array of size 3X+1, where every element occurs three times, except one element, 
#       which occurs only once. Find the element that occurs only once.

# Code

from collections import Counter

testCases = int(input("Enter number of test cases => "))

for _ in range(testCases):
    n = int(input("Enter n = "))
    nums = list(map(int, input("Enter list of numbers = ").split()))

    hashMap = Counter(nums)

    for number in hashMap:
        if hashMap[number] == 1: # if it occured only oncey - once
            print(f"The number that was repeated once is ==> {number}")


