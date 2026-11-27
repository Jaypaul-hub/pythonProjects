users = {}
while True:
    name=input("write your name here: ").strip()
    if name=="done":
       break
    status=input("write the status(active/inactive): ").strip()
    users[name]=status
print(users)