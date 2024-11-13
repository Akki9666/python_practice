# map, filter

arr = [1, 3, -2, 1, -23, -34]
positives = []
for i in range(len(arr)):
    if arr[i] > 0:
        positives.append(arr[i])
print(positives)

# filter(function, iterable)
print(list(filter(lambda x:x<0, arr)))

# map (function, iterable)
data = list(map(int, input("Enter nums: ").split()))
print(data)