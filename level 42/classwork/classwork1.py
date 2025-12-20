


data = []

def register():
    name = input("Enter your username: ")
    password = input("Enter your password: ")

    user = {
        "username": name,
        "password": password
    }


    for i in data:
        if i["username"] == name:
            print("This username already exists!")


    data.append(user)
    print("Registration successful!")

register()
register()
register() 

print(data)









data = []

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    current_user = {
        "username": username,
        "password": password
    }

    if len(data) == 0:
        print("registration comlete")
        data.append(current_user)

    elif len(data) > 0:
        for i in  data:
            if i["name"] == current_user["name"]:
                print("already exists")
                username = input   