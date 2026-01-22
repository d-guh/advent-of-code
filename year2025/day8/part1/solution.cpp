// Day 8: Playground, Part 1

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>

using namespace std;

static const string FILE_PATH = "../.input";

struct Point {
    long long x, y, z;
};

struct Edge {
    long long dist;
    int u, v;
    bool operator<(const Edge& other) const {  // For sort
        return dist < other.dist;
    }
};

class UnionFind {
public:
    vector<int> parent;
    UnionFind(int size) {
        parent.resize(size);
        iota(parent.begin(), parent.end(), 0);  // Sequential fill
    }

    int find(int i) {
        if (parent[i] == i) {
            return i;
        }

        parent[i] = find(parent[i]);  // Path compression
        return parent[i];
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

long long squared_distance(const Point& p1, const Point& p2) {
    long long dx = p2.x - p1.x;
    long long dy = p2.y - p1.y;
    long long dz = p2.z - p1.z;
    return (dx * dx) + (dy * dy) + (dz * dz);
}

int main() {
    vector<Point> junction_boxes;

    ifstream junction_boxes_file(FILE_PATH);
    string line;
    while (getline(junction_boxes_file, line)) {
        stringstream ss(line);
        string val;
        Point p;

        getline(ss, val, ','); p.x = stoll(val);
        getline(ss, val, ','); p.y = stoll(val);
        getline(ss, val, ','); p.z = stoll(val);

        junction_boxes.emplace_back(p);
    }
    junction_boxes_file.close();

    int num_boxes = junction_boxes.size();
    vector<Edge> all_pairs;
    for (int i = 0; i < num_boxes; ++i) {
        for (int j = i+1; j < num_boxes; ++j) {
            all_pairs.push_back({squared_distance(junction_boxes[i], junction_boxes[j]), i, j});
        }
    }

    sort(all_pairs.begin(), all_pairs.end());

    UnionFind uf(num_boxes);
    int limit = min(1000, (int)all_pairs.size());
    for (int i = 0; i < limit; ++i) {
        uf.unite(all_pairs[i].u, all_pairs[i].v);
    }

    map<int, int> counts;
    for (int i = 0; i < num_boxes; ++i) {
        counts[uf.find(i)]++;
    }

    vector<int> circuit_sizes;
    for (auto const& [root, size] : counts) {
        circuit_sizes.push_back(size);
    }
    sort(circuit_sizes.rbegin(), circuit_sizes.rend());  // Descending

    long long product = 1;
    int top_count = min((int)circuit_sizes.size(), 3);
    for (int i = 0; i < top_count; ++i) {
        product *= circuit_sizes[i];
    }

    cout << "Product: " << product << endl;

    return 0;
}
