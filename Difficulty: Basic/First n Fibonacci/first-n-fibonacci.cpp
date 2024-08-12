//{ Driver Code Starts
//Initial function template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++


class Solution
{
    public:
    //Function to return list containing first n fibonacci numbers.
    vector<long long> printFibb(int n) 
    {
        //code here
        
        
         vector<long long> nxt;  // Resultant vector

    if (n >= 1) nxt.push_back(1);  // Pehla Fibonacci number
    if (n >= 2) nxt.push_back(1);  // Dusra Fibonacci number

    long long t1 = 1, t2 = 1;
    for (int i = 3; i <= n; i++) {
        long long nxt1 = t1 + t2;  // Naya Fibonacci number calculate karte hain
        nxt.push_back(nxt1);  // Resultant vector mein add karte hain
        t1 = t2;  // Update karte hain t1 aur t2 ko
        t2 = nxt1;
    }

    return nxt; 
    }
};

//{ Driver Code Starts.
int main()
 {
     //taking total testcases
    int t;
    cin>>t;
    while(t--)
    {
        //taking number of elements
        int n;
        cin>>n;
        Solution obj;
        //calling function printFibb()
        vector<long long> ans = obj.printFibb(n);
        
        //printing the elements of vector
        for(long long i:ans)cout<<i<<' ';
        cout<<endl;
    }
	return 0;
}

// } Driver Code Ends