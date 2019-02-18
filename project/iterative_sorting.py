# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if (arr[j] <= arr[smallest_index]):
                smallest_index = j
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
    return arr


# my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
# print(my_arr)
# arr = selection_sort(my_arr)
# print(my_arr)

# TO-DO: implement the Insertion Sort function below


def insertion_sort(arr):
    # separate the first element from the rest of the array, think about it as a sorted list of one element
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i
        while (pos > 0 and arr[pos - 1] > current):
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = current
    return arr


# print(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))

# STRETCH: implement the Bubble Sort function below

# Walk through the array, comparing each element to its right neighbor. If it's smaller than that neighbor, swap the elements. Repeat this until you make it through an entire pass without any swaps.
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
