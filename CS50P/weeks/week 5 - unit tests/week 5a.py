from calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()



def test_positive():
    try:
        assert square(2) == 4
        assert square(3) == 9
    except AssertionError:
        print("postive error")

def test_negative():
    try:
        assert square(-2) == 4
        assert square(-3) == 9
    except AssertionError:
        print("negative error")

def test_zero():
    try:
        assert square(0) == 0 
    except AssertionError:
        print("zero error")
    



if __name__ == "__main__":
    main()