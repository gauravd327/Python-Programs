def LCM(num1, num2):

    firstnum = num1
    secondnum = num2

    while num1 != num2:
        if num1 < num2:
            num1 += firstnum
        if num2 < num1:
            num2 += secondnum
        if num1 == num2:
            return "LCM: " + str(num1)


print(LCM(22, 17))
