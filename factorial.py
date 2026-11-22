num=int(input("Enter any positive number: "))
if num<0:
    print("There is no factorial of negative number")
else:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"the factorial of {num} is {factorial}")