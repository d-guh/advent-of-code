// Day 1: Secret Entrance, Part 2

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

static const char* FILE_PATH = "../.input";
static const int DIAL_SIZE = 100;

int main() {
    int position = 50;
    int password = 0;

    ifstream contents(FILE_PATH);
    string line;

    while (getline(contents, line)) {
        //cout << "DEBUG: line: " << line << "\n";
        char direction = line[0];
        int magnitude = stoi(line.substr(1));
        //cout << "DEBUG: dir: " << direction << " mag: " << magnitude << "\n";

        //cout << "DEBUG: " << position;  // DEBUG GROUP1 PT1
        int dist_to_zero;
        switch (direction) {
            case 'L':
                if (position == 0) { dist_to_zero = DIAL_SIZE; } else { dist_to_zero = position; }
                position = ((position - magnitude) % 100 + 100) % 100;
                break;
            case 'R':
                if (position == 0) { dist_to_zero = DIAL_SIZE; } else { dist_to_zero = DIAL_SIZE - position; }
                position = (position + magnitude) % 100;
                break;
            default:
                cerr << "Invalid direction: (skipping " << line << ")\n";
                continue;
        }

        // Calculate number of times passing zero (includes landing)
        if (magnitude >= dist_to_zero) {
            password += 1 + (magnitude - dist_to_zero) / DIAL_SIZE;
        }

        //cout << " -> " << line << " -> " << position << "\n";  // DEBUG GROUP1 PT2
    }

    cout << "Password: " << password << endl;  // ANSWER: 5815

    return 0;
}
