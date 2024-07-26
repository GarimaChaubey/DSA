//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int isPerfect(int N) {
        // code here
        int originalN = N;
        int sum=0;
        while(N>0)
        {
            int digit=N%10;
            N=N/10;
            
            sum+=fact(digit);
        }
        
        if(sum==originalN)
        {
            return 1;
        }
        
        else
        {
            return 0;
        }
        
    }
    
    int fact(int n)
    {
        int fact=1;
        for (int i = 1; i <= n; ++i) 
        {
            fact *= i;
        }
        return fact;
    }
    
    
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        Solution ob;
        cout << ob.isPerfect(N) << "\n";
    }
}

// } Driver Code Ends