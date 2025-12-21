// Day 1: Secret Entrance, Part 2

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const string FILE_PATH = "../.input";

int main() {
    int position = 50;
    int count = 0;

    ifstream rotations_file(FILE_PATH);
    if (!rotations_file.is_open()) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    string line;
    while (getline(rotations_file, line)) {
        char direction = line[0];
        int value = stoi(line.substr(1));
        // This works but is slow due to 2D for loop w/ comparisons, see if better way using math trick?
        for (int i = 0; i < value; i++) {
            switch (direction) {
                case 'L':
                    position -= 1;
                    break;
                case 'R':
                    position += 1;
                    break;
                default:
                    cout << "How did you get here? (skipping " << line << ")" << endl;
                    continue;
            }
            position %= 100;  // Actual position
            count += (position == 0);  // Bool trick
        }
        // cout << "DEBUG: " << position << endl;
    }

    cout << "Final count: " << count << endl;

    return 0;
}
