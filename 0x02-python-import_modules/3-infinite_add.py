#!/usr/bin/python3
import sys
def calculate():
    arg_cal = sys.argv[1:]
    if arg_cal:
        total = 0
        for arg in arg_cal:
            total += int(arg)
            print(f"{total}")
    if __name__ == " __main__":
        calculate()
