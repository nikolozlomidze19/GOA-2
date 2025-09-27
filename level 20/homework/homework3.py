data = [123, "hello", 45.6, "world", True, "Python"]


for item in data:

    if type(item) == str:
      
        item_uppered = item.upper()
        
        print(item_uppered[-3:])


