// Day 5: Cafeteria, Part 1

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const string FILE_PATH = "../.input";

int main() {
    unsigned long long total_fresh = 0;
    vector<pair<unsigned long long, unsigned long long>> id_ranges;
    vector<unsigned long long> ingredient_ids;

    ifstream ids_file(FILE_PATH);
    string line;
    bool range_flag = true;

    while(getline(ids_file, line)) {
        if (line == "") {
            range_flag = false;
            continue;
        }
        if (range_flag) {
            size_t dash_pos = line.find('-');
            string first_str = line.substr(0, dash_pos);
            string second_str = line.substr(dash_pos + 1);
            //cout << "DEBUG: first: " << first_str << ", second: " << second_str << endl;

            unsigned long long first_num = stoull(first_str);
            unsigned long long second_num = stoull(second_str);

            id_ranges.emplace_back(make_pair(first_num, second_num));
        } else {
            ingredient_ids.emplace_back(stoull(line));
        }
    }

    for (const unsigned long long ingredient_id : ingredient_ids) {
        for (const pair<unsigned long long, unsigned long long>& range : id_ranges) {
            //cout << "DEBUG: " << range.first << ", " << ingredient_id << ", " << range.second << endl;
            if ((range.first <= ingredient_id) && (ingredient_id <= range.second)) {
                ++total_fresh;
                break;
            }
        }
    }

    //for (const pair<unsigned long long, unsigned long long>& range : id_ranges) {
    //    cout << "DEBUG: Range: " << range.first << "-" << range.second << "\n";
    //}
    //for (const unsigned long long ingredient_id : ingredient_ids) {
    //    cout << "DEBUG: ID: " << ingredient_id << "\n";
    //}
    cout << "Total Fresh IDs: " << total_fresh << endl;

    return 0;
}
