#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    n = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    for i in range(1, n):
        if argv[i] == 3:
            print("{} {} {} = {}".format(a, sys.argv[2], b, 
                operator[sys.argv[2]](a, b)))
        else:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")            
            exit(1)
