#include <iostream>
#include <map>

using namespace std;

int main() {
    string query;
    map<string,int> bag;

    while (cin >> query) {
        if (query == "store") {
                    string word;
                    cin >> word;

                        if (bag.find(word) == bag.end()) bag.insert(make_pair(word, 1));
                        else {
                            auto it = bag.find(word);
                            ++it->second;
        }
        }
    }
}