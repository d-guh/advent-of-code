#!/usr/bin/env python3
# Day 1: Secret Entrance, Part 2

import sys

FILE_PATH = "../.input"
DIAL_SIZE = 100

def main():
    position = 50
    password = 0

    contents = open(FILE_PATH, "r")

    for line in contents:
        line = line.strip()
        #print(f"DEBUG: line: {line}")
        direction = line[0]
        magnitude = int(line[1:])
        #print(f"DEBUG: dir: {direction} mag: {magnitude}")

        #print(f"DEBUG: {position}", end="")  # DEBUG GROUP1 PT1
        match direction:
            case 'L':
                dist_to_zero = DIAL_SIZE if position == 0 else position
                position = (position - magnitude) % DIAL_SIZE
            case 'R':
                dist_to_zero = DIAL_SIZE if position == 0 else DIAL_SIZE - position
                position = (position + magnitude) % DIAL_SIZE
            case _:
                print(f"Invalid direction: (skipping {line})", file=sys.stderr)
                continue

            # NOTE: The '%' operator in Python returns the Euclidean remainder
            # unlike other languages, that compute truncated remainder

        if (magnitude >= dist_to_zero):
            password += 1 + (magnitude - dist_to_zero) // DIAL_SIZE

        # NOTE: The '//' operator in python performs floor division
        # unlike other languages, which do this by default

        #print(f" -> {line} -> {position}")  # DEBUG GROUP1 PT2

    print(f"Password: {password}")  # ANSWER: 5815

if __name__ == "__main__":
    main()
