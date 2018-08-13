def sum_cal(n):
    a=0
    b=1
    for num in range(n):
        a=b
        b=a+b
        print(a)
    return a , b



Value = int(input("Enter the range value, n = "))
sum_cal(Value)