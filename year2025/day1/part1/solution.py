#!/usr/bin/env python3
# Day 1: Secret Entrance, Part 1

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
                position -= magnitude
            case 'R':
                position += magnitude
            case _:
                print(f"Invalid direction: (skipping {line})", file=sys.stderr)
                continue

        # Choice 1: % (euclidean remainder)
        # Most efficient, but you have to be careful about integer underflow/overflow
        #if (position % DIAL_SIZE) == 0:
        #    password += 1

        # Choice 2: %= (euclidean remainder & assignment)
        # Slightly less efficient, helps prevent integer flow issues
        # RECOMMENDED FOR DEBUG/VISUALS
        position %= DIAL_SIZE
        if position == 0:
            password += 1

        # NOTE: The '%' operator in Python returns the Euclidean remainder
        # unlike other languages, that compute truncated remainder

        #print(f" -> {line} -> {position}")  # DEBUG GROUP1 PT2

    print(f"Password: {password}")  # ANSWER: 1018

if __name__ == "__main__":
    main()
