//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    pair<long long, long long> getMinMax(vector<long long int> arr) {
        // code here
        long long maxi=arr[0];
        long long mini=arr[0];
        
        for(int i=0;i<arr.size();i++)
        {
            if(arr[i]>maxi)
            {
                maxi=arr[i];
            }
            
            else if(arr[i]<mini)
            {
                mini=arr[i];
            }
        }
        
        return {mini, maxi};
        
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<long long int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        pair<long long, long long> pp = ob.getMinMax(arr);
        cout << pp.first << " " << pp.second << endl;
    }
    return 0;
}
// } Driver Code Ends