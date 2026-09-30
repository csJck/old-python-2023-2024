
def main():
    convert(input("say something: "))
    

def convert(x):
    x = x.replace(":)","🙂").replace(":(","🙁")
    print(x)

main()
