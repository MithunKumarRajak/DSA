# Bubble Sort Algorithm in Python
arr = [12, 34, 23, 45, 67, 89, 90, 11, 9, 5]
# reverse False means accending order follow karna hai and reverse True mean decending order follow karna hai
# key = none , means abhi koi key value ya specific nuber ko find anhi kar rahe hai ,abhi apne adjcent number ko compare kar rahe hai
# accending order ke liye a>b and reverse = false
# decending order ke liye a<b and reverse = true

n = len(arr)


def bubble_sort(arr, reverse=False):
    swapped = False  # flag variable
    '''
# flag variable --> that acts as a signal or indicator inside a program.
It usually holds a True/False (boolean) value
to tell whether something has happened or has not happened.
(False)	Nothing happened yet
(True)	Something happened
    # '''
    swap_count = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
           # Yaha pe [j] wala part mai j current index represent kar raha hai
            a = arr[j]  # It's equivalent to arr[j+0] --> 0 means current index
            # Yaha pe [j+1] wala part mai j toh index represent kar raha hai aur +1 uske next index ko represent kar raha hai
            b = arr[j + 1]
            if (a > b and not reverse) or (a < b and reverse):
                # Yaha pe left side mai current and next element ki value assign hai or right side only order change karne se value swap ho gayi...
                # Swaping without temp variable
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ''' OR Other Method to swap using temp variable
                temp = arr[j]          # store current element in temp
                arr[j] = arr[j + 1]    # replace current element with next element
                arr[j + 1] = temp      # assign temp to next element
                '''
                swap_count += 1
                # swapped --> temporary flag (indicator variable) used inside the loop to check whether any swaps happend or not...
                swapped = True
        if not swapped:  # swapping not happend then break the loop
            break  # Stop the loop completely
        # continue--> Skip this iteration only
    return (arr, swap_count)


# if a function returns multiple values separated by commas, it always returns a single tuple containing those values.
# unpacking the returned tuple into two variables
arr, swap_count = bubble_sort(arr)
# syntax of tuple unpacking
# variable ,variable = (value) and * --> (Star for remaining values)

print("Sorted Array:", arr)
print("Total swaps:", swap_count)
