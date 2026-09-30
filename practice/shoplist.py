shoplist = dict()

while True:
    try:
        item = input()
        
        if item not in shoplist:
            shoplist[item] = 1
        
        else:
            shoplist[item] +=1
    

    except EOFError:
        break


for key, value in shoplist.items():
    print(value, key)



