// Day 3: Lobby, Part 1

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

const string FILE_PATH = "../.input";

int main() {
    unsigned long long total_joltage = 0;
    ifstream banks_file(FILE_PATH);
    string bank;

    while (getline(banks_file, bank)) {
        //string orig_bank = bank;  // Debug group
        // These are chars for display purposes, but behave the same with the exception of the ascii conversion when computing combined_joltage.
        char second_battery = bank.back();
        bank.pop_back();
        char first_battery = bank.back();
        bank.pop_back();

        reverse(bank.begin(), bank.end());  // Reverse shortened list for bubble sort type logic

        for (char battery : bank) {
            //cout << "DEBUG: battery: " << battery << endl;
            if (battery >= first_battery) {
                //cout << "DEBUG: replacing first_battery " << first_battery << " -> " << battery << endl;
                char temp_battery = first_battery;
                first_battery = battery;
                battery = temp_battery;
            } else { continue; }
            if (battery >= second_battery) {
                //cout << "DEBUG: replacing second_battery " << second_battery << " -> " << battery << endl;
                second_battery = battery;
            }
        }

        unsigned combined_joltage = (first_battery - '0')*10 + (second_battery - '0');
        //cout << "DEBUG: " << (first_battery - '0')*10 << ", " << (second_battery - '0') << endl;
        //cout << "DEBUG: " << orig_bank << ": " << combined_joltage << endl;  // Debug group
        total_joltage += combined_joltage;
    }

    cout << "Total Joltage: " << total_joltage << endl;
    return 0;
}
