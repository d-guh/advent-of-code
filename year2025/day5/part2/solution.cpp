// Day 5: Cafeteria, Part 2

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const string FILE_PATH = "../.input";

bool compare(const pair<unsigned long long, unsigned long long>& i, const pair<unsigned long long, unsigned long long>& j) {
    return i.first < j.first;
}

int main() {
    unsigned long long total_fresh = 0;
    vector<pair<unsigned long long, unsigned long long>> id_ranges;
    vector<pair<unsigned long long, unsigned long long>> merged_ranges;

    ifstream ids_file(FILE_PATH);
    string line;

    while(getline(ids_file, line)) {
        if (line == "") {
            break;
        }
        size_t dash_pos = line.find('-');
        string first_str = line.substr(0, dash_pos);
        string second_str = line.substr(dash_pos + 1);

        unsigned long long first_num = stoull(first_str);
        unsigned long long second_num = stoull(second_str);

        id_ranges.push_back(make_pair(first_num, second_num));
    }

    sort(id_ranges.begin(), id_ranges.end(), compare);
    // for (const pair<unsigned long long, unsigned long long>& range : id_ranges) {
    //     cout << "DEBUG: Orig Range: " << range.first << "-" << range.second << "\n";
    // }

    for (const pair<unsigned long long, unsigned long long>& cur_range : id_ranges) {
        if ((merged_ranges.empty()) || merged_ranges.back().second < cur_range.first) {
            merged_ranges.push_back(cur_range);
        } else {
            merged_ranges.back().second = max(merged_ranges.back().second, cur_range.second);
        }
    }

    // for (const pair<unsigned long long, unsigned long long>& range : merged_ranges) {
    //     cout << "DEBUG: Merged Range: " << range.first << "-" << range.second << "\n";
    // }

    for (const pair<unsigned long long, unsigned long long>& range : merged_ranges) {
        total_fresh += range.second - range.first + 1;
    }

    cout << "Total Fresh IDs: " << total_fresh << endl;

    return 0;
}
