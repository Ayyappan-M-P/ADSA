def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    
    return arr

# Input array
input_array = [10, 2, 7, 1, 5, 3]

# Using Bubble Sort
sorted_array_bubble = bubble_sort(input_array)
print("Bubble Sort Result:", sorted_array_bubble)

# Using Python's built-in sorted function
sorted_array_builtin = sorted(input_array)
print("Python's built-in sorted Result:", sorted_array_builtin)

# Time Complexity Analysis
# (Already explained in the previous response)

# Stability Analysis
# Bubble Sort is stable, maintaining the relative order of equal elements
