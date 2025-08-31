name="nick"
age=14
#print(name+age)   #შეცდომა,str ს და int ს ვერ დავუმატებთ

print(name+str(age)) #სწორი გზა

#print(hello world!) #შეცდომა როდესაც ცვლადი პირველად გამოგვაქვს ბრჭყალები სჭირდება
print("hello world") #სწორი გზა

#print(name) #შეცდომა ,თანმიმდევრობა არ არის დაცული
#name=nick

name="nick" #სწორი გზა
print(name)

#color->red   #შეცდომა, საჭიროა ტოლობის ნიშანი
color="red" #სწორი გზა

#name=nick #შეცდომა, str ს ბრჭყალები სჭირდება
name="nick" #სწორი გზა
