def selectionsort(n):
    for x in range(len(n)):
        minimum = x
        for i in range(len(n)):
            if n[minimum] < n[i]:
                n[minimum], n[i] = n[i], n[minimum]

    return n


list_to_sort = [8, 2, 1, 5, 9, 3, 7, 6, 4]

print("Unsorted list: " + str(list_to_sort))

print("\n")

print("Sorted_list: " + str(selectionsort(list_to_sort)))