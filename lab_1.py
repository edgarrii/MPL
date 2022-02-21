arr = [0, 1, 2, 3, 4, 5, 6]
i = 0

while i < len(arr):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    i+=2
    if (i == len(arr) - 1):
        break
    

print(arr)