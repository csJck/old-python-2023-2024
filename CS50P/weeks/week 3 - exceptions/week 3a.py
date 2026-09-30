def main():
   print(f"int is {get_int("what's x? ")}")
    

def get_int(prompt):
  while True:
      try:
          x = int(input(prompt))

      except ValueError:
        print("x must be an integer")

      # else can be used inside try blocks, what this else statement is doing is basically saying that if an error doesnt occur then do this:
      else:
          return x
    
  

main()

