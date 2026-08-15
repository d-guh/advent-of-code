// Day 1: Secret Entrance, Part 1

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
        switch (direction) {
            case 'L':
                position -= magnitude;
                break;
            case 'R':
                position += magnitude;
                break;
            default:
                cerr << "Invalid direction: (skipping " << line << ")\n";
                continue;
        }

        // Choice 1: % (truncated remainder)
        // Most efficient, but you have to be careful about integer underflow/overflow
        //if ((position % DIAL_SIZE) == 0) {
        //    password += 1;
        //}

        // Choice 2: %= (truncated remainder & assignment)
        // Slightly less efficient, helps prevent integer flow issues
        position %= DIAL_SIZE;
        if (position == 0) {
            password += 1;
        }

        // Choice 3: (euclidean remainder)
        // Less efficient, but clamps to "real" positive values, has integer flow issues
        // NOT RECOMMENDED (this is a bit silly without a tempvar/function)
        //if (((position % DIAL_SIZE) + DIAL_SIZE) % DIAL_SIZE == 0) {
        //    password += 1;
        //}

        // Choice 4: (euclidean remainder & assignment)
        // Least efficient, but "real" positional record, helps prevent integer flow issues
        // RECOMMENDED FOR DEBUG/VISUALS
        //position = ((position % DIAL_SIZE) + DIAL_SIZE) % DIAL_SIZE;
        //if (position == 0) {
        //    password += 1;
        //}
        // NOTE: assignment can also be written as:
        //position %= DIAL_SIZE;
        //if (position < 0) position += DIAL_SIZE;

        //cout << " -> " << line << " -> " << position << "\n";  // DEBUG GROUP1 PT2
    }

    cout << "Password: " << password << endl;  // ANSWER: 1018

    return 0;
}
