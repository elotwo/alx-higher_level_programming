#!/usr/bin/python3
import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_args = len(arguments)
    print(f"{num_args} arguments:")
    if num_args > 0:
        n = 1
        for arg in arguments:
            print(f"{n}: {arg}")
            n += 1
if __name__ == "__main__":
    print_arguments()
