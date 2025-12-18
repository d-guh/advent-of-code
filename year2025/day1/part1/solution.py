#!/usr/bin/env python3
# Day 1: Secret Entrance, Part 1

FILE = "../.input"

def main():
    position = 50
    count = 0

    with open(FILE, 'r') as rotations_file:
        for line in rotations_file:
            direction = line[0]
            value = int(line[1:])

            match direction:
                case 'L':
                    position -= value
                    # print(f"DEBUG: {line.strip()}: {position}")
                case 'R':
                    position += value
                    # print(f"DEBUG: {line.strip()}: {position}")
                case _:
                    print(f"How did you get here? (skipping {line.strip()})")
                    continue

            position %= 100  # Calculates actual position
            count += (position == 0)  # Funny bool moment
            # print(f"DEBUG: {position}")

    print(f"Final count: {count}")

if __name__ == "__main__":
    main()
