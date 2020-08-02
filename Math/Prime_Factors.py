import time
start = time.time()
def prime_check(num):
    y = num
    prime_list = [2]
    iters = 3
    for x in range(num):
        count = 1     
        factor_list = []
        for x in range(iters):
            if iters % count == 0:
                factor_list.append(count)
                
            elif iters % count == 1:
                pass
            count += 1
        
        if len(factor_list) > 2:
            iters += 1

        else:
            prime_list.append(iters)
            iters += 1

    count = 0
    pf = []
    while num > 1:
        if num % prime_list[count] != 0:
            count += 1
            continue

        pf.append(prime_list[count])

        num //= prime_list[count]

    print("The prime factors of " + str(y) + " are:")
    print(pf)

    return ""


print(prime_check(5050))
end = time.time()
print("Time taken: " + str(end - start) + " seconds")
