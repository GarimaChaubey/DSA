//{ Driver Code Starts
 
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	

	string removeCharacters(string S) 
	{
	    // Your code goes here
	    /*string res="";
	    for(int i=0;i<=S.length()-1;i++)
	    {
	        if(S[i]>=0 && S[i]<=9)
	        {
	            res+=S[i];
	        }
	        else 
	        {
	            continue;
	        }
	    }
	    
	    return res;
	    */
	    
	    string res = "";
    for (char ch : S) 
    {
        if (ch >= '0' && ch <= '9') 
        {
            res += ch;
        }
    }
    return res;
	}
};

//{ Driver Code Starts.

int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string s;
   		cin >> s;
   		Solution ob;
   		cout << ob.removeCharacters(s) << "\n";
   		
   	}

    return 0;
}
// } Driver Code Ends