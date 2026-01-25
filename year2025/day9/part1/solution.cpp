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

    size_t num_tiles = red_tiles.size();
    unsigned long long max_area = 0;
    for (size_t i = 0; i < num_tiles; ++i) {
        for (size_t j = 0; j < num_tiles; ++j) {
            unsigned long long cur_area = area(red_tiles[i], red_tiles[j]);
            //cout << "DEBUG: " << red_tiles[i].x << "," << red_tiles[i].y << " * " << red_tiles[j].x << "," << red_tiles[j].y << " = " << cur_area << "\n";
            if (cur_area > max_area) {
                max_area = cur_area;
            }
        }
    }

    cout << "Largest area: " << max_area << endl;

    return 0;
}
