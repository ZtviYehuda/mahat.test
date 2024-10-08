def is_triangular_array(arr):
    l = len(arr)

    if l % 3 != 0:
        return False

    slice = l // 3
    slice_a = arr[:slice]
    slice_b = arr[slice:slice * 2]
    slice_c = arr[slice * 2:]

    return slice_a == slice_b == slice_c

arr = [9,8,9,8,9,8]
print(is_triangular_array(arr))