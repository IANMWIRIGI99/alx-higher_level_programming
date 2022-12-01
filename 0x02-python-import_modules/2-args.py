#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    no_of_elements = len(argv) - 1
    if no_of_elements == 1:
        print(f"{no_of_elements} argument:")
        print(f"{no_of_elements}: {argv[-1]}")
    if no_of_elements > 1:
        print(f"{no_of_elements} arguments:")
    while(i < no_of_elements):
        print(f"{i}: {argv[i]}")
        i += 1
if no_of_elements > 1:
    print(f"{no_of_elements}: {argv[-1]}")
if no_of_elements == 0:
    print(f"{no_of_elements} arguments.")
