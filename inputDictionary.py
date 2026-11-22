n=int(input("enter the initial number in a range: "))
m=int(input("enter the final number in a range: "))
for num in range(n,m):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
         