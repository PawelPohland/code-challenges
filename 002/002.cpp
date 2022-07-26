#include <iostream>

using namespace std;

// n! = 1 * 2 * ... * (n - 1) * n
int factorial1(int number) {
    int result = 1;

    for (int i = 1; i <= number; i++)
        result *= i;

    return result;
}

// n! = 1 * 2 * ... * (n - 2) * (n-1)! * n
int factorial2(int number) {
    if (number <= 1)
        return 1;

    return factorial2(number - 1) * number;
}

int main() {
    cout << "Enter a number: ";

    string input;
    cin >> input;

    int number = stoi(input);

    cout << input << "! = " << factorial1(number) << endl;
    cout << input << "! = " << factorial2(number) << endl;

    return 0;
}