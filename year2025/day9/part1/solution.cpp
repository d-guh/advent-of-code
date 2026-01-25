// Day 9: Movie Theater, Part 1

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

static const string FILE_PATH = "../.input";

struct Tile {
    long x, y;
};

unsigned long long area(const Tile& t1, const Tile& t2) {
    long width = abs(t2.x - t1.x) + 1;
    long height = abs(t2.y - t1.y) + 1;
    return static_cast<unsigned long long>(width) * static_cast<unsigned long long>(height);
}

int main() {
    // Vector for O(1) insert to back, duplicates unlikely, accessing in order, not searching
    vector<Tile> red_tiles;

    ifstream red_tiles_file(FILE_PATH);
    string line;
    while (getline(red_tiles_file, line)) {
        stringstream ss(line);
        string val;
        Tile t;

        getline(ss, val, ','); t.x = stoul(val);
        getline(ss, val, ','); t.y = stoul(val);

        red_tiles.emplace_back(t);
    }
    red_tiles_file.close();

    unsigned long long max_area = 0;
    // Using iterators rather than indicies, skips checking self, skips reverse order repeats, still O(n^2), but less iterations
    for (auto it1 = red_tiles.begin(); it1 != red_tiles.end(); ++it1) {
        for (auto it2 = next(it1); it2 != red_tiles.end(); ++it2) {
            unsigned long long cur_area = area(*it1, *it2);
            //cout << "DEBUG: " << it1->x << "," << it1->y << " * " << it2->x << "," << it2->y << " = " << cur_area << "\n";
            max_area = max(max_area, cur_area);
        }
    }

    cout << "Largest area: " << max_area << endl;

    return 0;
}
