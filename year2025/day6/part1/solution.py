#!/usr/bin/env python3
# Day 6: Trash Compactor, Part 1

FILE_PATH = "../.input"

def main():
    total = 0
    worksheet = []

    with open(FILE_PATH, 'r') as worksheet_file:
        worksheet = [line.split() for line in worksheet_file]
    
    worksheet = [tuple(row[::-1]) for row in zip(*worksheet)]

    # print(f"DEBUG: {worksheet}")

    operator = ''
    value = 0
    for equation in worksheet:
        # There's either a lapse in my knowledge or C++ is much better suited for this lol
        for i, op in enumerate(equation):  # Operator or operand
            if i != 0:
                #print(f"DEBUG: op: {value} {operator} {op} = ", end='')
                if operator == '+':
                    value += int(op)
                elif operator == '*':
                    value *= int(op)
                #print(value)
            else:
                operator = op
                if operator == '+':
                    value = 0
                elif operator == '*':
                    value = 1
        #print(f"DEBUG: tot: {total} + {value} = ", end='')
        total += value
        #print(total)

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
