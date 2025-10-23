# arr = [5, 2, 8, 1]
# arr = ['apple', 'kiwi', 'banana', 'orange']
arr = [(2, 'apple'), (1, 'banana'), (3, 'Cucumber'), (2, 'date')]


def bubble_sort_key(arr, key=None, reverse=False):
    n = len(arr)
    swap_count = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            # key function provided
            a = key(arr[j]) if key else arr[j]  # swaping logic
            b = key(arr[j + 1]) if key else arr[j + 1]  # swaping logic

            if (a > b and not reverse) or (a < b and reverse):  # codition to swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swap_count += 1
                swapped = True

        if not swapped:
            break

    return arr, swap_count


# Sort numbers normally
# due to tuple returned by function and unpacking here
sorted_arr, total_swaps = bubble_sort_key(arr)
print("Sorted Array:", sorted_arr)
print("Total swaps:", total_swaps)


# Sort strings by length
sorted_arr, total_swaps = bubble_sort_key(arr, key=len)
print("Sorted by length:", sorted_arr)


# Sort tuples by second element or alphabetically
sorted_arr, total_swaps = bubble_sort_key(arr, key=lambda x: x[1])
print("Sorted by second element:", sorted_arr)
