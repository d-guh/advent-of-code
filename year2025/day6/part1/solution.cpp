// Day 6: Trash Compactor, Part 1

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
    vector<vector<string>> worksheet;
    // Not transposing input for memory/speed sake?
    ifstream worksheet_file(FILE_PATH);
    string line;
    while(getline(worksheet_file, line)) {
        istringstream iss(line);
        vector<string> row((istream_iterator<string>(iss)), istream_iterator<string>());  // Constructor shenanigans

        worksheet.push_back(row);
    }

    // for (const vector<string>& equation : worksheet) {
    //     cout << "DEBUG: ";
    //     for (const string& op : equation) {
    //         cout << op << " ";
    //     }
    //     cout << endl;
    // }

    size_t numRows = worksheet.size();
    size_t numCols = worksheet[0].size();

    for (size_t i = 0; i < numCols; i++) {
        // I lied this is still buns, i should've transposed lol
        const string operatorSign = worksheet[numRows - 1][i];  // Last row (operator)
        unsigned long long value = (operatorSign == "+") ? 0 : 1;  // Avoid multiply by 0

        for (size_t j = 0; j < numRows - 1; j++) {
            const string& operand = worksheet[j][i];
            // cout << "DEBUG: op: " << value << " " << operatorSign << " " << operand << " = ";
            if (operatorSign == "+") {
                value += stoull(operand);
            } else if (operatorSign == "*") {
                value *= stoull(operand);
            }
            // cout << value << endl;
        }
        // cout << "DEBUG: tot: " << total << " + " << value << " = ";
        total += value;
        // cout << total << endl;
    }

    cout << "Total: " << total << endl;

    return 0;
}
