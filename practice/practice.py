notes = {}
x = 0

while True:
    x += 1
    try:
        note = input()
        notes[note] = x

    except EOFError:
        break



for key, value in notes.items():
    print(value, key)
        