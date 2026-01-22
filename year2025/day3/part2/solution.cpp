// Day 3: Lobby, Part 2

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const string FILE_PATH = "../.input";

int main() {
    unsigned long long total_joltage = 0;
    unsigned num_batteries = 12;

    ifstream banks_file(FILE_PATH);
    string bank;

    while (getline(banks_file, bank)) {
        // These are chars for display purposes, but behave the same with the exception of the ascii conversion when computing combined_joltage.
        vector<int> batteries;

        for (size_t i = bank.size() - num_batteries; i < bank.size(); ++i) {
            batteries.emplace_back(bank[i] - '0');  // Convert to int
        }

        //cout << "DEBUG: starting batteries: ";
        //for (int c : batteries) {
        //    cout << c;
        //}
        //cout << endl;

        string remaining_bank = bank.substr(0, bank.size() - num_batteries);  // Shrink bank
        reverse(remaining_bank.begin(), remaining_bank.end());  // Reverse bank

        for (char cur_battery_char : remaining_bank) {
            int cur_battery = cur_battery_char - '0';
            //cout << "DEBUG: cur_battery: " << cur_battery << endl;
            for (size_t j = 0; j < batteries.size(); ++j) {
                if (cur_battery < batteries[j]) {
                    break;
                }
                //cout << "DEBUG: Replacing " << batteries[j] << " -> " << cur_battery << endl;
                int temp_battery = batteries[j];
                batteries[j] = cur_battery;
                cur_battery = temp_battery;
            }
        }

        unsigned long long combined_joltage = 0;
        for (int joltage : batteries) {
            combined_joltage = (combined_joltage * 10) + joltage;
        }
        //cout << "DEBUG: " << bank << ": " << combined_joltage << endl;
        total_joltage += combined_joltage;
    }

    cout << "Total Joltage: " << total_joltage << endl;
    return 0;
}
