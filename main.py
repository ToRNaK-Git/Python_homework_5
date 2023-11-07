arr = []
a = int(len(arr) / 2)
b = int((1 + len(arr) / 2))
if len(arr) % 2 == 0:
    new_arr = ([arr[:a], arr[a:]])
    print(new_arr)
elif len(arr) % 2 == 1:
    new_arr = ([arr[:b], arr[b:]])
    print(new_arr)
else:
    new_arr = ([], [])
    print(new_arr)
