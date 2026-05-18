# Rearrange Sequence - 1 
#       You are given an array of size N containing unique integers. 
#       Find the size of the largest subarray that can be rearranged to form a contiguous sequence.

#       A contiguous sequence means that the difference of adjacent elements should be 1.




#       Explained with sample test case

#       Example
        # Input
        # 2
#        Test Case 1
        # 5
        # 1 3 2 6 5
#        Test Case 2
        # 9
        # 0 8 6 5 7 10 3 2 1

        # Output
        # 3
        # 4

        # Explanation

        # Test-Case 1
        # The largest subarray that can be rearranged to form a contiguous sequence is [1, 3, 2] 
        # which can be rearranged to form [1, 2, 3].

        # Test-Case 2
        # The largest subarray that can be rearranged to form a contiguous sequence is [8, 6, 5, 7] 
        # which can be rearranged to form [5, 6, 7, 8].



# Code

testCases = int(input("Enter number of test cases => "))

for _ in range(testCases):
    n = int(input("Enter n = "))
    nums = list(map(int, input("Enter list of numbers = ").split()))

    ans = 0
    for i in range(n): # normal iteration
        low = high = nums[i]
        for j in range(i,n): # checking every possible subarray
            low = min(low, nums[j])
            high = max(high, nums[j])

            if (j - i + 1) == (high - low + 1): # now here is the catch, we check if the max number and min diff + 1 
                                                # and the indexes diff + 1 is same, then we can say that there is no
                                                # missing number
                                                # say low = 10 and high = 12 (these are values)
                                                # and say i = 0 and j = 1 (these are indices)
                                                # now j - i + 1 = 2
                                                # but high - low + 1 = 3
                                                # there is a missing number here [which is 11 here](since 2 != 3)
                ans = max(ans, j - i + 1)
    
    print(ans)
