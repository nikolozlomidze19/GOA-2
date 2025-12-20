# 2)შექმენით სია სადაც გექნებათ მოცემული სახელები, შემდეგ ახალ სიაში ჩაამატეთ ისეთი სახელები სახელები რომლის სიმბოლოების რაოდენობაც არის ლუწი რიცხვი
names = ["Nick", "Giorgi", "Mariami", "Ani", "Daviti", "Tamari", "Luka"]

even_names = [i for i in names if len(i) % 2 == 0]

print(names)
print(even_names)

