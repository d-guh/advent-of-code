// Day 4: Printing Department, Part 2

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const string FILE_PATH = "../.input";

void print_diagram(const vector<vector<bool>>& diagram) {
    for (const vector<bool>& row : diagram) {
        for (bool col : row) {
            cout << (col ? '@' : '.');
        }
        cout << endl;
    }
    cout << string(diagram.size(), '=') << endl;
}

bool check_surrounding(const vector<vector<bool>>& diagram, int x, int y) {
    //cout << "DEBUG: Checking surrounding for " << x << "," << y << endl;
    int count = 0;
    vector<pair<int, int>> directions = {
        {0, -1},  // N
        {1, 0},   // E
        {0, 1},   // S
        {-1, 0},  // W
        {1, -1},  // NE
        {1, 1},   // SE
        {-1, 1},  // SW
        {-1, -1}, // NW
    };

    for (const pair<int, int>& direction : directions) {
        int dx = direction.first;
        int dy = direction.second;
        int nx = x + dx;
        int ny = y + dy;
        if (nx >= 0 && nx < diagram.size() && ny >= 0 && ny < diagram[0].size()) {
            //cout << "DEBUG: Position at " << nx << "," << ny << " (offset " << dx << ", " << dy << ") is " << diagram[ny][nx] << endl; 
            if (diagram[ny][nx]) {
                ++count;
            }
        }
    }

    return (count < 4);
}

int main() {
    unsigned long long accessible_rolls = 0;
    unsigned long long prev_accessible_rolls = 0;
    vector<vector<bool>> stored_diagram;

    ifstream diagram_file(FILE_PATH);
    string line;

    while (getline(diagram_file, line)) {
        vector<bool> bool_line;
        for (char c : line) {
            bool_line.emplace_back(c == '@');
        }
        stored_diagram.emplace_back(bool_line);
    }

    diagram_file.close();

    do {
        prev_accessible_rolls = accessible_rolls;
        for (size_t y = 0; y < stored_diagram.size(); ++y) {
            for (size_t x = 0; x < stored_diagram[y].size(); ++x) {
                //cout << "DEBUG: " << x << "," << y << ": " << stored_diagram[y][x] << endl;
                if (stored_diagram[y][x]) {
                    if (check_surrounding(stored_diagram, x, y)) {
                        ++accessible_rolls;
                        stored_diagram[y][x] = false;
                    }
                }
            }
        }
    } while (accessible_rolls != prev_accessible_rolls);

    //print_diagram(stored_diagram);
    cout << "Total Accessible Rolls: " << accessible_rolls << endl;

    return 0;
}
