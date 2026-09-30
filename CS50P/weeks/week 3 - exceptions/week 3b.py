def main():
    pyramid(int(input("pyramid height: ")))

def pyramid(n):
    for i in range(n+1):
        print(" " * n,"[]" * i, " " * n)
        n -= 1

main()