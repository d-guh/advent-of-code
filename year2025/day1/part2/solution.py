#!/usr/bin/env python3
# Day 1: Secret Entrance, Part 2

FILE = "../.input"

def main():
    position = 50
    count = 0

    with open(FILE, 'r') as rotations_file:
        for line in rotations_file:
            direction = line[0]
            value = int(line[1:])
            # This works but is slow due to 2D for loop w/ comparisons, see if better math trick or something
            for _ in range(value):
                match direction:
                    case 'L':
                        position -= 1
                    case 'R':
                        position += 1
                    case _:
                        print(f"How did you get here? (skipping {line.strip()})")
                        continue

                position %= 100
                count += (position == 0)
            # print(f"DEBUG: {position}")

    print(f"Final count: {count}")

if __name__ == "__main__":
    main()
