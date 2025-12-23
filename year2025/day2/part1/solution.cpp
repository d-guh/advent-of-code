// Day 2: Gift Shop, Part 1

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const string FILE_PATH = "../.input";

int main() {
    unsigned long long invalid_total = 0;

    ifstream ids_file(FILE_PATH);
    if (!ids_file.is_open()) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    string id_range;
    while (getline(ids_file, id_range, ',')) {
        // cout << "DEBUG: each range: " << id_range << endl;
        string start_id = id_range.substr(0, id_range.find("-"));
        string end_id = id_range.substr(id_range.find("-")+1, id_range.length());
        // cout << "DEBUG: split range: " << start_id << "-" << end_id << endl;
        unsigned long long start_id_num = stoull(start_id);  // even unsigned long too small lol
        unsigned long long end_id_num = stoull(end_id);
        // cout << "DEBUG: num range: " << start_id_num << "-" << end_id_num << endl;
        for (unsigned long long cur_id = start_id_num; cur_id < end_id_num; cur_id++) {
            string cur_id_str = to_string(cur_id);
            unsigned int length = cur_id_str.length();
            // cout << "DEBUG: len: " << length << endl;

            if (length % 1 == 0) {  // Only check even IDs
                // cout << "DEBUG: checking: " << cur_id << endl;
                unsigned int half_length = length / 2;
                string first_half = cur_id_str.substr(0, half_length);
                string second_half = cur_id_str.substr(half_length, length);
                // cout << "DEBUG: first second: " << first_half << " " << second_half << endl;


                if (first_half == second_half) {
                    // cout << "DEBUG: MATCH: " << cur_id << endl;
                    invalid_total += cur_id;
                }
            }
        }
    }
    cout << invalid_total << endl;

    return 0;
}
