// Day 7: Laboratories, Part 1

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
    unsigned long long split_count = 0;
    vector<vector<char>> manifold;

    ifstream manifold_file(FILE_PATH);
    string line;
    while (getline(manifold_file, line)) {
        manifold.emplace_back(line.begin(), line.end());
    }
    manifold_file.close();

    //cout << "DEBUG: starting manifold:\n";
    //print_manifold(manifold);

    for (char& c : manifold[0]) {
        if (c == SOURCE) {
            c = TACHYON_BEAM;
            break;
        }
    }

    for (size_t i = 0; i < manifold.size() - 1; i++) {
        for (size_t j = 0; j < manifold[i].size(); j++) {
            //cout << "DEBUG: manifold[" << i << "][" << j << "]: " << manifold[i][j] << "\n";
            if (manifold[i][j] == TACHYON_BEAM) {
                if (manifold[i+1][j] == EMPTY_SPACE) {
                    manifold[i+1][j] = TACHYON_BEAM;
                } else if (manifold[i+1][j] == SPLITTER) {
                    split_count++;
                    if (manifold[i+1][j-1] == EMPTY_SPACE) {
                        manifold[i+1][j-1] = TACHYON_BEAM;
                    }
                    if (manifold[i+1][j+1] == EMPTY_SPACE) {
                        manifold[i+1][j+1] = TACHYON_BEAM;
                    }
                }
            }
        }
    }

    //cout << "DEBUG: ending manifold:\n";
    //print_manifold(manifold);

    cout << "Total splits: " << split_count << endl;

    return 0;
}
