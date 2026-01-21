// Day 7: Laboratories, Part 2

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

#define SOURCE 'S'
#define TACHYON_BEAM '|'
#define EMPTY_SPACE '.'
#define SPLITTER '^'

static const string FILE_PATH = "../.input";

void print_manifold(const vector<vector<char>>& manifold) {
    for (const auto& row : manifold) {
        for (const char c : row) {
            cout << c;
        }
        cout << '\n';
    }
}

int main() {
    vector<vector<char>> manifold;

    return 0;
}
