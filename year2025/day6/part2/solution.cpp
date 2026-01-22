// Day 6: Trash Compactor, Part 2

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

const string FILE_PATH = "../.input";

int main() {
    unsigned long long total = 0;
    vector<string> worksheet;

    ifstream worksheet_file(FILE_PATH);
    string line;
    while(getline(worksheet_file, line)) {
        worksheet.emplace_back(line);
    }
    worksheet_file.close();

    // Debug for reading in OK
    //for (const string& row : worksheet) {
    //    cout << "DEBUG: " << row << endl;
    //}

    vector<tuple<vector<int>, char>> worksheet_collapsed;
    vector<int> numbers;

    size_t max_rows = worksheet.size();
    size_t max_columns = worksheet[0].size();

    // Not full transpose since storing 1 col at a time, probably slow though
    for (size_t col = max_columns; col > 0; col--) {
        string col_chars;
        for (size_t row = 0; row < max_rows; ++row) {
            if (col - 1 < worksheet[row].size()) {
                col_chars.push_back(worksheet[row][col - 1]);
            }
        }

        string number_str(col_chars.begin(), col_chars.end() - 1);
        char operator_char = col_chars.back();
        number_str.erase(remove(number_str.begin(), number_str.end(), ' '), number_str.end());
        if (!number_str.empty()) {
            numbers.emplace_back(stoi(number_str));
        }
        if (operator_char != ' ') {
            worksheet_collapsed.emplace_back(tuple(numbers, operator_char));
            numbers.clear();
        }
    }

    // Debug for confirming collapse
    //cout << "[";
    //for (const auto& row : worksheet_collapsed) {
    //    const vector<int> intVector = get<0>(row);
    //    const char op = get<1>(row);
    //    cout << "(";
    //    for (size_t j = 0; j < intVector.size(); ++j) {
    //         cout << intVector[j];
    //        if (j < intVector.size() - 1) {
    //            cout << ", ";
    //        }
    //    }
    //    cout << ", '" << op << "') ";
    //}
    //cout << "]" << endl;

    for (const tuple<vector<int>, char>& equation : worksheet_collapsed) {
        const vector<int>& ops = get<0>(equation);
        char operator_char = get<1>(equation);
        unsigned long long value = (operator_char == '+') ? 0 : 1;

        for (int op : ops) {
            if (operator_char == '+') {
                value += op;
            } else {
                value *= op;
            }
        }
        total += value;
    }

    cout << "Total: " << total << endl;

    return 0;
}
