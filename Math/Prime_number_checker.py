def prime_check(num):
    if num  <= 0:
        return "Invalid input"
    elif num == 1:
        return "1 is neither prime nor composite"
    elif num == 2:
        return "2 is a prime number"
    else:
        count = 1
        factor_list = []
        for x in range(num):
            if num % count == 0:
                factor_list.append(count)
                
            elif num % count == 1:
                pass
            count += 1
        if len(factor_list) > 2:
            return str(num) + " is not a prime number\n\nFactors: " + str(factor_list)
        else:
            return str(num) + " is a prime number"
    
    
print(prime_check(140))
