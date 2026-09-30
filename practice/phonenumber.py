def create_phone_number(n):
    
    num = ''.join(map(str,n))
   
    part1 = num[0:3]
    part2 = num[3:6]
    part3 = num[6:]

    y = f"({part1}) {part2}-{part3}"

    print(y)

    
  

create_phone_number([1,2,3,4,5,6,7,8,9,8])