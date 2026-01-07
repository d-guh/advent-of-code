#!/usr/bin/env python3
# Day 3: Lobby, Part 1

FILE_PATH = "../.input"

def main():
    total_joltage = 0

    with open(FILE_PATH, 'r') as banks_file:
        for bank in banks_file:
            bank = bank.strip()
            # print(f"DEBUG: bank: {bank}")
            first_battery = int(bank[-2])
            second_battery = int(bank[-1])
            
            # Slightly less ugly alternate solution, should be much better in part2, will be abstracted
            for battery in map(int, bank[:-2][::-1]):  # Reverse for bubble sort logic
                # print(f"DEBUG: battery: {battery}")
                if battery > first_battery:
                    # print(f"DEBUG: replacing first_battery {first_battery} -> {battery}")
                    battery, first_battery = first_battery, battery
                else: continue
                if battery > second_battery:
                    # print(f"DEBUG: replacing second_battery {second_battery} -> {battery}")
                    second_battery = battery
                # print("")
            
            combined_joltage = first_battery * 10 + second_battery
            # print(f"DEBUG: combined: {combined_joltage}")
            total_joltage += combined_joltage
    print(f"Total Joltage: {total_joltage}")

if __name__ == "__main__":
    main()
