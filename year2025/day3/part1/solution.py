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
            
            # This is a very ugly solution, will improve for part 2 since it seems that one could be abstracted anyways
            # I made an alternate version that may be easier to understand but is slightly less performant logic wise
            # All of these issues will be address in part2
            for battery in map(int, bank[:-2][::-1]):  # Reverse for bubble sort ish
                # print(f"DEBUG: battery: {battery}")
                if battery <= first_battery:
                    # print("")
                    continue
                # print(f"DEBUG: replacing first_battery {first_battery} -> {battery}")
                battery, first_battery = first_battery, battery  # Swap, old 1st battery value is passed for 2nd check
                if battery <= second_battery:
                    # print("")
                    continue
                # print(f"DEBUG: replacing second_battery {second_battery} -> {battery}")
                second_battery = battery
                # print("")
            
            combined_joltage = first_battery * 10 + second_battery
            # print(f"DEBUG: combined: {combined_joltage}")
            total_joltage += combined_joltage
    print(f"Total Joltage: {total_joltage}")  # 17212 too low

if __name__ == "__main__":
    main()
