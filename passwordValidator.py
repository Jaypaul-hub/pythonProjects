password= input("Enter strong password: ")
isUpper=False
isLowe=False
isDigit=False
for i in password:
    if i.isupper():
        isUpper=True
    elif i.islower():
        isLower=True
    elif i.isdigit():
        isDigit=True
if len(password)<8:
    print("password should be atleast 8 characters")
elif not isUpper:
    print("password must atleast has one upper letter")
elif not isLower:
    print("password must atleast has one lower letter")
elif not isDigit:
    print("password must atleast has one digit")
else:
    print("The password is correct")


