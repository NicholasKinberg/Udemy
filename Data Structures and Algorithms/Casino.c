#include <iostream>
#include <map>

using namespace std;

int main() {
    int x;
    string name, op;
    map<string, int> m;
    map<string, int>::iterator it;
    while (cin >> name >> op) {
        if (op == "enters") {
            it = m.find(name);
            if (it != m.end()) cout << name << " is already in the casino" << endl;
            else m.insert(make_pair(name, 0));
        }

        else if (op == "wins") {
            cin >> x;
            it = m.find(name);
            if (it == m.end()) cout << name << " is not in the casino" << endl;
            else it->second += it->second + x;
        }
        else if (op == "leaves") {
            it = m.find(name);
            if (it == m.end()) cout << name << " is not in the casino" << endl;
            else {
                cout << it->first << " has won " << it->second << endl;
                m.erase(name);
            }
        }
        if (name == "end") break;
    }

        cout << "----------" << endl;

        for (it = m.begin(); it != m.end(); ++it) {
            cout << it->first << " is winning " << it->second << endl;
        }
}