#include <iostream>
#include <map>

using namespace std;

map<int, int> genDictionary(int max_key) {
    map<int, int> dictionary;

    for (int i = 1; i <= max_key; i++) {
        dictionary[i] = i * i;
    }

    return dictionary;
}

void printDictionary(map<int, int> dictionary) {
    map<int, int>::iterator iter;

    cout << "{";

    int counter = 1;

    for (iter = dictionary.begin(); iter != dictionary.end(); iter++) {
        cout << (*iter).first << ": " << (*iter).second;
        if (counter != dictionary.size()) {
            cout << ", ";
        }
        counter++;
    }

    cout << "}" << endl;
}

int main() {
    string user_input;

    cout << "Enter a number: ";
    cin >> user_input;

    int max_key = stoi(user_input);

    map<int, int> dictionary = genDictionary(max_key);
    printDictionary(dictionary);
    
    return 0;
}