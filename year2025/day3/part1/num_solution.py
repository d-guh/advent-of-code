#!/usr/bin/env python3
# Day 3: Lobby, Part 1

FILE_PATH = "../.input"

def main():
    total_joltage = 0

    with open(FILE_PATH, 'r') as banks_file:
        for bank in banks_file:
            bank = bank.strip()
            # print(f"DEBUG: bank: {bank}")
            # Doing these operations as ints, could also be strings, this may improve comparisons but makes concat different, also requires map in for loop
            first_battery = int(bank[-2])
            second_battery = int(bank[-1])
            
            # This is a sort of ugly solution, but the logic is there, will be abstraced/improved in part 2
            for battery in map(int, bank[:-2][::-1]):  # Reverse for bubble sort logic
                # print(f"DEBUG: battery: {battery}")
                if battery >= first_battery:
                    # print(f"DEBUG: replacing first_battery {first_battery} -> {battery}")
                    battery, first_battery = first_battery, battery
                else: continue
                if battery >= second_battery:
                    # print(f"DEBUG: replacing second_battery {second_battery} -> {battery}")
                    second_battery = battery
                # print("")
            
            combined_joltage = first_battery * 10 + second_battery  # Numerical form of concatenation
            # print(f"DEBUG: {bank}: {combined_joltage}")
            total_joltage += combined_joltage
    print(f"Total Joltage: {total_joltage}")

if __name__ == "__main__":
    main()
