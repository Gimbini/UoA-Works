
def min_subarray_sums():
    first_input = input()
    data = first_input.split()
    list_size = int(data[0])
    m = int(data[1])
    array = []

    for i in range(list_size):
        array.append(int(input()))
        
    j = 0
    sub_array = array[j:m]
    min_sub_array = sum(sub_array)
    for i in range(list_size - m):
        j += 1
        m += 1
        new_sub_array = array[j:m]

        min_sub_array = min(min_sub_array, sum(new_sub_array))

    print(min_sub_array)

min_subarray_sums()
