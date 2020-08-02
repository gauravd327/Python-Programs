import numpy as np
import time


def binary_search(nlist, n):
    for x in range(len(nlist) - 1):
        if nlist[0] == n:
            return True
        middle = len(nlist) // 2

        if n < nlist[len(nlist) // 2]:
            nlist = nlist[0:middle]

        else:
            nlist = nlist[middle::]

    return False


start = time.time()
sample_list = np.arange(1, 100001)
if binary_search(sample_list, 1):
    print("Element found at index ")

else:
    print("Element not found")
end = time.time()

print("\n")
print("Time taken: " + str(end - start) + "seconds")
