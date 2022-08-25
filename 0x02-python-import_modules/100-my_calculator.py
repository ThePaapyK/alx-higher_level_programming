#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    gen = ['+', '-', '*', '/']
    s = 0
    for i in range(len(gen)):
        if (argv[2] == gen[i]):
            s = -1
            break
        else:
            s = s + 1

    if s >= 4:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

        a = int(argv[1])
        b = int(argv[3])

        if (s == -1):
            if (argv[2] == '+'):
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif (argv[2] == '-'):
                print("{:d} * {:d} = {:d}".format(a, b, sub(a, b)))
            elif (argv[2] == '*'):
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            elif (argv[2] == '/'):
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
