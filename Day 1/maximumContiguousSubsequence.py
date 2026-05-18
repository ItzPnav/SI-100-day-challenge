# Maximum Contiguous Subsequence 
#           Given an array, find the length of the longest subsequence whose 
#           elements can be re-arranged in a strictly increasing contiguous order. 
#           The difference between 2 adjacent elements in the subsequence, after re-arrangement, should be exactly 1.

# Code

testCases = int(input("Enter number of test cases => "))

for _ in range(testCases):
    n = int(input("Enter n = "))
    nums = list(map(int, input("Enter list of numbers = ").split()))

    nums.sort()

    count = 0
    ans = 0

    temp = nums[0]

    for i in range(1, n):
        if nums[i] == temp:
            continue
        elif nums[i] == temp + 1:
            count += 1
        else:
            count = 0
        
        temp = nums[i]
        ans = max(ans, count + 1)
    print(f"Maximum Contiguous Subsequence length is {ans}")

