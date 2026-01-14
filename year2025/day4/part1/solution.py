#!/usr/bin/env python3
# Day 4: Printing Department, Part 1

FILE_PATH = "../.input"

def print_diagram(diagram: list[list[bool]]) -> None:
    for row in diagram:
        print(''.join('@' if col else '.' for col in row))
    print('=' * len(diagram))

def check_surrounding(diagram: list[list[bool]], x: int, y: int) -> bool:
    # print(f"DEBUG: Checking surrounding for {x},{y}")
    count = 0
    directions = [
        (0, -1),  # N
        (1, 0),   # E
        (0, 1),   # S
        (-1, 0),  # W
        (1, -1),  # NE
        (1, 1),   # SE
        (-1, 1),  # SW
        (-1, -1), # NW
    ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(diagram) and 0 <= ny < len(diagram[0]):
            # print(f"DEBUG: Position at {nx},{ny} (offset {dx}, {dy}) is {diagram[ny][nx]}")
            if diagram[ny][nx]:
                count += 1

    return (count < 4)

def main():
    accessible_rolls = 0
    stored_diagram = []

    with open(FILE_PATH, 'r') as diagram_file:
        for line in diagram_file:
            bool_line = [char == '@' for char in line.strip()]
            stored_diagram.append(list(bool_line))

    for y, row in enumerate(stored_diagram):
        for x, col in enumerate(row):
            # print(f"DEBUG: {x},{y}: {stored_diagram[y][x]}")
            if col:
                if check_surrounding(stored_diagram, x, y):
                    accessible_rolls += 1

    #print_diagram(stored_diagram)
    print(f"Total Accessible Rolls: {accessible_rolls}")

if __name__ == "__main__":
    main()
