//{ Driver Code Starts
//Initial template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution{
    public:
/*	int fullPrime(int N){
	    //code here
	    if(!isprime(N))
	    {
	        return 0;
	    }
	    int num=N;
	    while(num>0)
	    {
	        int digit=N%10;
	            if(!isprime(digit))
	            {
	                return 0;
	            }
	            num=num/10;
	        
	    }
	    
	    return 1;
	}
	
	bool isprime(int n)
	{
	    if (n <= 1) return false;
	    for(int i = 2; i <= n/2; ++i) 
	    {
            if(n%i == 0) 
            {
                return false;
            }
        }
        return true;
	}*/
	bool isprime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int fullPrime(int N) {
    // Pehle check karte hain agar N prime hai ya nahi
    if (!isprime(N)) {
        return 0;
    }

    int num = N;
    while (num > 0) {
        int digit = num % 10;
        if (!isprime(digit)) {
            return 0;
        }
        num = num / 10;
    }

    return 1;
}

};


//{ Driver Code Starts.
int main()
{
	int t;
    cin>>t;
    while(t--){
	   int N;
	   cin>>N;
       Solution ob;
       cout << ob.fullPrime(N)<<"\n";
    }
}
// } Driver Code Ends