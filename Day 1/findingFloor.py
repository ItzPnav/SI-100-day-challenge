# Finding the Floor 

#       Given an array, you have to find the floor of a number x. 
#       The floor of a number x is nothing but the largest number 
#       in the array less than or equal to x.


# Code

n = int(input("Enter n = "))

arr = list(map(int, input("Enter numbers with a space = ").split()))

arr.sort()

queries = int(input("How many queries do u want to run = "))

for _ in range(queries):
    x = int(input("Enter x = "))

    if x < arr[0]:
        print(-2147483648)
        print(f"    The floor of {x} is = -2147483648")
        continue

    left = 0
    right = n - 1
    
    found = False

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            found = True
            break
        
        elif arr[mid] > x:
            right = mid - 1
        
        else:
            left = mid + 1
    
    if found:
        print(f"    The floor of {x} is = {x}")
    
    else:
        print(f"    The floor of {x} is = {arr[right]}")