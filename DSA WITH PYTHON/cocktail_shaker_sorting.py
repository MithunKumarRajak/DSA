# Version of bubble sorting --> cocktail shaker sorting('two-way movement' --> reduces the number of passes roughly by half)
arr = [25, 56, 89, 22, 8, 6, 4, 10, 4,]


def cocktail_shaker_sorting(arr):
    n = len(arr)
    if n <= 1:  # elements in array is 0 or 1: already sorted
        return arr
    start = 0
    end = n - 1
    swapped = True  # to enter the while loop or not with condition swapped

    while swapped and start < end:
        swapped = False
        # forward pass
        for i in range(start, end):
            # arr[i] or arr[j] --> it’s just variable naming — i and j...
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        # reset swapped for backward pass
        swapped = False
        # Since the largest element is now sorted at the end, we can ignore that index in the next round.
        end = end - 1

        # backward pass
        for i in range(end, start, -1):  # range(start, stop, step)
            '''
            # start  -> where counting begins (inclusive)
            # stop   -> where counting stops (exclusive)
            # step   -> how much to increment/decrement each time
            # By default, step = 1 → counts forward (increment by 1 each time)
            # If step = -1 → counts backward (decrement by 1 each time)
            # This is used in backward pass of cocktail shaker sort
            '''
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        # Since the smallest element is now sorted at the start, we can ignore that index in the next round.
        start = start + 1

    return arr


print(cocktail_shaker_sorting(arr))
