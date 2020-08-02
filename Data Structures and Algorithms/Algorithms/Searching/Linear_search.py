import time
import numpy as np


def linear_search(nlist, n):
    for x in range(len(nlist)):
        if nlist[x] == n:
            return True

    return False


start = time.time()
sample_list = np.arange(1, 100001)
if linear_search(sample_list, 1):
    print("Element found")

else:
    print("Element not found")
end = time.time()

print("\n")
print("Time taken: " + str(end - start) + "seconds")
