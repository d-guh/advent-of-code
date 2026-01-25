// Day 9: Movie Theater, Part 2

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

static const string FILE_PATH = "../.temp";

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

    unsigned long long max_area = 0;

    return 0;
}
