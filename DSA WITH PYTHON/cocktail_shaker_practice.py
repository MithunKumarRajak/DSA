'''
1. define arr
2. define function
3. check length of arr
4. initialize start, end, swapped variables
5. while loop with condition swapped and start < end
6. forward pass with for loop from start to end
7. if arr[i] > arr[i + 1], swap and set swapped to True, swapped=true because we want to continue the while loop
8. if not swapped, break
9. reset swapped for backward pass
10. decrement end by 1
11. backward pass with for loop from end to start in reverse
12. if arr[i - 1] > arr[i], swap and set swapped to True
13. increment start by 1
14. return sorted arr 
'''
arr = [10, 18, 16, 4, 12, 14]


def cocktail_shaker_sorting(arr):

    n = len(arr)
    if n <= 1:
        return arr
    start = 0
    end = n - 1
    swapped = True
    pass_num = 1  # To track the number of passes
    forward_swaps = 0  # to count number of swaps in each direction
    backward_swaps = 0
    while swapped and start < end:
        swapped = False
        for i in range(start, end):
            if arr[i] < arr[i + 1]:  # changes come here for descending order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                forward_swaps += 1
                print(
                    f"Pass {pass_num} - Forward: {arr}  Swaps: {forward_swaps}")
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end, start, -1):
            if arr[i - 1] < arr[i]:  # changes come here for descending order
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
                backward_swaps += 1
                print(
                    f"Pass {pass_num} - Backward: {arr}  Swaps: {backward_swaps}")

        start = start + 1
        pass_num += 1  # Increment pass number after each full forward and backward pass
    return arr


sorted_arr = cocktail_shaker_sorting(arr)
print("Sorted array:", sorted_arr)

sorted_arr = cocktail_shaker_sorting(arr)
# another method for descending order
descending_arr = sorted_arr[::-1]  # Reverse using slicing or [-1:len(arr):1]
'''
list[start:stop:step]
start → starting index (default 0)
stop → ending index (default len(list))
step → step size (default 1)
'''
print(descending_arr)
