# Sum of Subarrays 
#           Given an array of integers, answer queries of the form: [i, j]: Print the sum of array elements from A[i] to A[j], 
#           both inclusive.

# Code

n = int(input("Enter n = "))

arr = list(map(int, input("Enter numbers with a space = ").split()))

# to solve this problem
# we use prefix sum array

prefixSumArray = [0] * n

prefixSumArray[0] = arr[0]

for i in range(1, n):
    prefixSumArray[i] = prefixSumArray[i - 1] + arr[i]

prefixSumArray = [0] + prefixSumArray

queries = int(input("How many queries do u want to run = "))

for _ in range(queries):
    start, end = map(int, input("Enter start, end values = ").split())

    print(f"    The subarray({arr[start:(end + 1)]})  sum is = {prefixSumArray[end + 1] - prefixSumArray[start]}")