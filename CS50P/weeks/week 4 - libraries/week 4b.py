import statistics as stat
import sys

print(stat.mean([80,87])) # works out the average or mean


if len(sys.argv) < 3:
    sys.exit("too few arguments") # ends the program


for arg in sys.argv[1:]:    
    print(f"Hello, my name is {arg}.") # sys.argv can take text from the console and store it a variable (arg)