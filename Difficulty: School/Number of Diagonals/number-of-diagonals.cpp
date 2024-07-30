//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	long long diagonals(long long n)
	{
		// Your code goes here
		
		return (n*(n-3))/2;

	}
};

//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

	   

	    Solution ob;
	    cout << ob.diagonals(n) << "\n";
   
    }
    return 0;
}

// } Driver Code Ends