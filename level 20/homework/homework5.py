animals = ["Dog", "Cat", "Lion", "tiger", "Wolf"]

for i in animals:
    if len(i) <= 5 and i.istitle():
        print(i[:3])   
    else:
        print("this word is long")