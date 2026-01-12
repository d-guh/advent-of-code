#!/usr/bin/env python3
# Day 3: Lobby, Part 2

FILE_PATH = "../.input"

def main():
    total_joltage = 0
    num_batteries = 12

    with open(FILE_PATH, 'r') as banks_file:
        for bank in banks_file:
            bank = bank.strip()  # Clean list
            remaining_bank = list(map(int, bank))  # Convert to ints
            # print(f"DEBUG: bank: {bank}")
            batteries = remaining_bank[-num_batteries:]  # Fill with specified amount of batteries from end of list
            # print(f"DEBUG: starting batteries: {''.join(map(str,batteries))}")
            
            for cur_battery in remaining_bank[:-num_batteries][::-1]:
                # print(f"DEBUG: cur_battery: {cur_battery}")
                for i, battery in enumerate(batteries):
                    # print(f"DEBUG: {cur_battery}, {battery}")
                    if cur_battery < battery:
                        break
                    # print(f"DEBUG: Replacing {battery} -> {cur_battery}")
                    cur_battery, battery = battery, cur_battery
                    batteries[i] = battery
            
            combined_joltage = 0
            for joltage in batteries:
                combined_joltage = combined_joltage * 10 + joltage
            # print(f"DEBUG: {bank}: {combined_joltage}")
            total_joltage += combined_joltage
    print(f"Total Joltage: {total_joltage}")

if __name__ == "__main__":
    main()
