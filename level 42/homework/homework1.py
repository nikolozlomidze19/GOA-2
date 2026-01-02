data = [] # შევქმენით data list (ცარიელი)

def register():     #register ფუნქცია შევქმენით
    username = input("Enter your username:")        #შემოვატანინოთ მომხმარებელს username
    password = input("Create a new password:")      #შემოვატანინოთ მომხმარებელს password
    current_user = {                                #შევქმენით current_user dictionary
        "name":username,                            #name-ს გადავეცით value-დ username
        "password":password                         #password-ს გადავეცით value-დ password
    }
    if len(data) == 0:                              #თუ data list-ის სიგრძე არის 0 მაშინ დაპრინტავს Registration successfull!
        print("Registration successfull!")
        data.append(current_user)                   #data list-ში დაამატებს current user-ში ჩასმულ მნიშვნელობას
    
    elif len(data) > 0:                             #elif data list-ის სიგრძე მეტია 0-ზე 
        for i in data:                              #დავიწყეთ for cycle
            if i["name"] == current_user["name"]:   #თუ სახელი და current_user-ში ჩასმული მნიშვნელობები ემთხვევა  
                print("username already exists!")   #დაპრინტავს username already exists!
                username = input("Enter another username again: ")       #შემოვატანინოთ მომხმარებს user_name ახლიდან რადგან ისინი ერთანეთს დაემთხვა
                current_user["name"] = username                          
                data.append(current_user)                                #data list-ში დავამატებთ curren_user-ს
                break
            else:                                                        #სხვა ნებისმიერ შემთხვევაში 
                print("Registration successfull!")                       #დაპრინტავს Registration successfull!
                data.append(current_user)                                #data list-ში დავამატებთ current_user-ს
                break                                                    #break for loop წყვიტავს

def login():                                                             #შევქმენით ახალი function სახელად login
    username = input("Enter your username: ")                            #შემოვატანინოთ მომხმარებელს username     
    password = input("Enter your password: ")                            #შემოვატანინოთ მომხმარებელს password
    
    for i in data:                                                          
        if i["name"] == username:                                        #თუ მომხმარებლისგან შემოყვანილი username და name ემხვევა ერთმანეთს
            if i["password"] == password:                                #და თუ მომხმარებლისგან შემოყვანილი password და password ემხვევა ერთმანეთს
                print("Login successful!")                               #მა
                return True
            else:
                print("Incorrect password!")
                return False
    
    print("Username not found!")
    return False

register()
register()
register()
print(data)


login()

