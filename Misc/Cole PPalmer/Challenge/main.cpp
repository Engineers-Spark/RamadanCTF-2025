#include <bits/stdc++.h>
#define ll long long
#define sz size
#define pk push_back
#define pok pop_back
#define forf(i, n) for (ll i = 0; i < n; i++)
#define rforf(i, n) for (int i = n - 1; i >= 0; i--)
using namespace std;
int main() {
    cout << "My friend Cole PPalmer has a variable t='0001000' and he wants to change it to 16." << endl;
    this_thread::sleep_for(chrono::seconds(1));
    cout << "0001000 -----> 16" << endl;
    this_thread::sleep_for(chrono::seconds(1));
    cout << "How?" << endl;
    cout << "Your solution > ";
    string k;
    cin >> k;
    if (k == "t.to_ulong()"||k == "t.to_ullong()") {
        cout << "Result = 16" << endl;
        cout << "Good!" << endl;
        this_thread::sleep_for(chrono::seconds(1));
        cout << "Now I have a vector B = [83, 112, 97, 114 ... and other integers]." << endl;
        this_thread::sleep_for(chrono::seconds(1));
        cout << "And I want to convert the values of the vector B to their binary representation." << endl;
        cout << "For example: x = 83 -----> 0000000001010011" << endl;
        this_thread::sleep_for(chrono::seconds(1));
        cout << "How?" << endl;
        cout << "Your solution > ";
        cin >> k;
        if (k == "bitset<16>(x)"||k == "bitset<16>x") {
            cout << "EXCELLENT!!!!!!" << endl;
            cout << "The result:" << endl;
            this_thread::sleep_for(chrono::seconds(1));
            vector<int> v = {83, 112, 97, 114, 107, 123, 49, 95, 76, 48, 118, 101, 95, 66, 49, 116, 95, 83, 51, 116, 95, 67, 43, 43, 125};
            forf(i, v.size()) {
                cout << v[i] << " ---> " << bitset<16>(v[i]) << endl;
            }
        } else if (k == "bitset<16> binary(x)") {
            cout << "You are too close, but why did you use chat?" << endl;
        } else {
            cout << "NOPE!" << endl;
            cout << "You need to learn more!" << endl;
        }
    } else if(k=="t.to_string()"){
        cout<<"You areeee to clooosee"<<endl;
        cout<<"Search moree"<<endl;
    }else {
        cout << "You need to learn more!" << endl;
    }
}