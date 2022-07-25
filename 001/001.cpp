#include <iostream>
#include <vector>

using namespace std;

vector<int> getNumbers(int startNum = 2000, int endNum = 3200) {
    vector<int> numbers;

    for (int number = startNum; number <= endNum; number++) {
        if (number % 7 == 0 && number % 5 != 0) {
            numbers.push_back(number);
        }
    }

    return numbers;
}

int main() {
    vector<int> numbers = getNumbers();

    for (int index = 0; index < numbers.size(); index++) {
        if (index != 0) {
            cout << ", ";
        }
        cout << numbers[index];
    }
    
    return 0;
}