#include <bits/stdc++.h>
#include <unistd.h>
#define ll long long
#define sz size
#define pk push_back
#define pok pop_back
using namespace std;
int binarySearch(const vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    int iterations = 0;
    while (low <= high) {
        iterations++;
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return iterations;
        }
        else if (arr[mid] < target) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return -1;
}

bool containsOnlyOneFifty(const vector<ll>& table) {
    int count = 0;
    for (ll num : table) {
        if (num == 50) {
            count++;
        }
    }
    return count == 1;
}
int main() {
    cout << "OxL4rti asked you if you can solve this challenge." << endl;
    cout << "He has just 6 questions for you to answer." << endl;
    cout << "Here is his magic table:" << endl;
    sleep(1);
    srand(time(0));
    set<int> OxL4rti;  
    while (OxL4rti.size() < 20) {
        OxL4rti.insert(rand() % 101);
    }
    cout << "|";
    vector<int> table(OxL4rti.begin(), OxL4rti.end());
    sort(table.begin(), table.end());
    for (const auto& num : table) {
        cout << num << "|";
    }
    cout << endl;
    vector<int> v = {table[10], table[4], table[17], table[6], 101, -1}; 
    for (int i = 0; i < 6; i++) {
        int result = binarySearch(table, v[i]);
        cout << "Target " << v[i] << " found in: ";
        ll k;
        cin >> k;
        if (k == result) {
            cout << "GOOD" << endl;
        } else {
            cout << "Wrong Answer" << endl;
            exit(1);
            return 0;
        }
    }
    sleep(1);
    cout << "YOU ARE SOOO SMART!" << endl;
    cout << "Before I give you the flag, I have another small challenge." << endl;
    cout << "Create a table by yourself." << endl;
    cout << "I want the number 50 to be found in 0 operations" << endl;
    ll p;
    cout << "Give me the length of your table: ";
    cin >> p;
    while (p < 10) {
        cout << "Invalid table length! Try number bigger" << endl;
        cout << "Give me the length of your table: ";
        cin >> p;
    }
    cout << "Give me the numbers: " << endl;
    vector<ll> a(p);
    for (int i = 0; i < p; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    if(!containsOnlyOneFifty(a)){
        cout<<"Yezzi bla gahchha"<<endl;
        exit(0);
        
    }
    if (a[p/2]==50||a[p/2-1]==50) {
        cout << "OOOHHHHH genius!" << endl;
        cout << "Here is the flag : Spark{B1n4ry_S34rch_4lg0}" << endl;
    } else {
        cout << "Oops, the number 50 is either missing or appears more than once!" << endl;
        exit(1);
    }

    return 0;
}
