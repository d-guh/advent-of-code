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
    vector<vector<char>> worksheet_matrix;

    ifstream worksheet_file(FILE_PATH);
    string line;
    while(getline(worksheet_file, line)) {
        vector<char> row(line.begin(), line.end());
        worksheet_matrix.push_back(row);
    }
    worksheet_file.close();

    // Debug for reading in OK
    // for (const vector<char>& row : worksheet_matrix) {
    //     cout << "DEBUG: ";
    //     for (const char col : row) {
    //         cout << col;
    //     }
    //     cout << endl;
    // }

    vector<vector<char>> worksheet_transposed;
    size_t max_columns = worksheet_matrix[0].size();
    for (size_t col = 0; col < max_columns; col++) {
        vector<char> col_chars;

        for (size_t row = 0; row < worksheet_matrix.size(); row++) {
            if (col < worksheet_matrix[row].size()) {
                col_chars.push_back(worksheet_matrix[row][col]);
            }
        }

        if (any_of(col_chars.begin(), col_chars.end(), [](char c) { return c != ' '; })) {
            worksheet_transposed.push_back(col_chars);  // Add non-empty columns
        }
    }

    // Debug for confirming transpose
    // for (const vector<char>& row : worksheet_transposed) {
    //     cout << "DEBUG: ";
    //     for (const char col : row) {
    //         cout << col;
    //     }
    //     cout << endl;
    // }

    vector<tuple<vector<int>, char>> worksheet_collapsed;
    vector<int> numbers;
    for (auto it = worksheet_transposed.rbegin(); it != worksheet_transposed.rend(); it++) {
        const vector<char>& col = *it;
        string number_str(col.begin(), col.end() - 1);
        char operator_char = col.back();
        numbers.push_back(stoi(number_str));
        if (operator_char != ' ') {
            worksheet_collapsed.push_back(tuple(numbers, operator_char));
            numbers.clear();
        }
    }

    // Debug for confirming collapse
    // cout << "[";
    // for (const auto& row : worksheet_collapsed) {
    //     const vector<int> intVector = get<0>(row);
    //     const char op = get<1>(row);
    //     cout << "(";
    //     for (size_t j = 0; j < intVector.size(); ++j) {
    //         cout << intVector[j];
    //         if (j < intVector.size() - 1) {
    //             cout << ", ";
    //         }
    //     }
    //     cout << ", '" << op << "') ";
    // }
    // cout << "]" << endl;

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
