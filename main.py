arr = [1, 2, 3]
a = int(len(arr) / 2)
b = int((1 + len(arr) / 2))
if len(arr) % 2 == 0:
    new_arr = ([arr[:a], arr[a:]])
else:
    new_arr = ([arr[:b], arr[b:]])
print(new_arr)
