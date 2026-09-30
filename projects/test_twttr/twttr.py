
def main():
    print(shorten(input("Input: ")))

def shorten(word):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    short = ""
    for x in range(len(word)):
        if word[x] not in vowels:
            short += word[x]

    return short



if __name__ == "__main__":
    main()
