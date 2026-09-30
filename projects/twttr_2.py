

def main():
    shorten(input("Input: ").lower())
   

def shorten(word):
    word = word.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
    


if __name__ == "__main__":
    main()
