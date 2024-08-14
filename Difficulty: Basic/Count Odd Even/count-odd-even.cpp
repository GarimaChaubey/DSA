//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    /*Function to count even and odd elements in the array
     * arr : Array with its elements
     */
    vector<int> countOddEven(vector<int> &arr) {
        // your code here
        
        int cnt1=0;
        int cnt2=0;
        vector<int>res;
        for(int i=0;i<arr.size();i++)
        {
            if(arr[i]%2==0)
            {
                cnt1++;
            }
            else 
            {
                cnt2++;
            }
        }
        
        res.push_back(cnt2);
        res.push_back(cnt1);
        
        return res;
    }
};

//{ Driver Code Starts.
int main() {

    // Testcase input
    int testcase;
    cin >> testcase;
    cin.ignore();

    while (testcase--) {
        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;

        vector<int> res = ob.countOddEven(arr);
        for (auto t : res) {
            cout << t << " ";
        }
        cout << endl;
    }

    return 0;
}
// } Driver Code Ends