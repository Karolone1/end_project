def flatten(nested_list):
    flattened_list = []

    for element in nested_list:
        if type(element) == list:
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)

    return flattened_list

nested_list = [[1, 2, [3]], 4]

flattened_list = flatten(nested_list)
print(flattened_list)