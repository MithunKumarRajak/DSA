arr = [12, 34, 23, 45, 53, 45, 84, 98, 54]


def bubble_sort(arr, reverse=False):
    n = len(arr)
    swap_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            a = arr[j]
            b = arr[j + 1]

            # Compare according to reverse flag
            if (a > b and not reverse) or (a < b and reverse):
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True

                # 👇 print current swap details
                # Here arrow is just like text
                print(f"Swap {swap_count}: swapped {a} and {b} → {arr}")
                '''
                This is an f-string (formatted string literal) in Python.
                It allows you to insert 'variable values' directly inside the string using { }.
                eg.
                name = "Mithun"
                print(f"My name is {name}")
                # Output: My name is Mithun


                '''

        if not swapped:
            break

    return arr, swap_count


sorted_arr, total_swaps = bubble_sort(arr)
print("\nFinal Sorted Array:", sorted_arr)
print("Total Swaps:", total_swaps)
