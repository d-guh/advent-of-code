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

int main() {
    unsigned long long total_timelines = 0;
    vector<vector<char>> manifold;

    ifstream manifold_file(FILE_PATH);
    string line;
    while (getline(manifold_file, line)) {
        manifold.emplace_back(line.begin(), line.end());
    }
    manifold_file.close();

    size_t num_rows = manifold.size();
    size_t num_cols = manifold[0].size();

    unsigned long counts[num_rows][num_cols] = {0};

    for (size_t j = 0; j < num_cols; j++) {
        if (manifold[0][j] == SOURCE) {
            counts[0][j] = 1;
            break;
        }
    }

    for (size_t r = 0; r < num_rows - 1; r++) {
        for (size_t c = 0; c < num_cols; c++) {
            //cout << "DEBUG: manifold[" << r << "][" << c << "]: " << manifold[r][c] << "\n";
            //cout << "DEBUG: counts[" << r << "][" << c << "]: " << counts[r][c] << "\n";
            unsigned long count = counts[r][c];
            if (count == 0) {
                continue;
            }

            char below = manifold[r+1][c];

            if (below == SPLITTER) {
                counts[r+1][c-1] += count;  // Left
                counts[r+1][c+1] += count;  // Right
            } else {
                counts[r+1][c] += count;  // Bring down
            }
        }
    }

    for (size_t j = 0; j < num_cols; j++) {
        total_timelines += counts[num_rows-1][j];
    }

    cout << "Total timelines: " << total_timelines << endl;

    return 0;
}
