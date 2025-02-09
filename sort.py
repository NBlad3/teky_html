list1 = [12, 45, 61, 31, 10, 51, 79, 9, 20]
list2 = [21, 16, 75, 89, 34, 62, 47, 1, 68]

def bubble_sort(arr):
    n = len(arr)
    steps = 0
    for i in range(n - 1):
        for j in range(0, n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, steps

sorted_arr, steps = bubble_sort(list1)

print(f"The sorted array is {', '.join(map(str, sorted_arr))}. It took {steps} steps.")