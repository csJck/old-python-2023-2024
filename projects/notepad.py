notepad = dict()
x = 0
print("\nwriting notes...........")

while True:
    x += 1
    try:
        note = input()
        notepad[note] = x
        
    except EOFError:
        break
        
print("-----NOTES-----")
for key, value in notepad.items():
    print("|",value,"."," ", key, sep="")