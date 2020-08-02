def bubblesort(n):
    for i in range(len(n) - 1):
        for x in range(len(n) - 1):
            if n[x] > n[x + 1]:
                n[x], n[x + 1] = n[x + 1], n[x]
    return n


list_to_sort = [8, 2, 1, 5, 9, 3, 7, 6, 4]

print("Unsorted list: " + str(list_to_sort))

print("\n")

print("Sorted_list: " + str(bubblesort(list_to_sort)))
