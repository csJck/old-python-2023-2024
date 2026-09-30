def main():
    print(hello("jack"))
    

#here i have set a default value of "name" this way if i use the function with no argument then it will default to saying hello user rahter than hello (name)
def hello(name="user"):
    return f"hello, {name}"
    

if __name__ == "__main__":
    main()