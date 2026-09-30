def solution(string):
    temp = list(string)
    text = temp
    
    for x in range(len(string)):
        text[x-1] = string[-x]
    
    for i in text:
        print(i,end="",sep="")

   
 
solution(input())