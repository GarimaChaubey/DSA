//{ Driver Code Starts
// Driver function
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    string reciprocalString(string S)
    {
        // Write Your code here
        
        string res;
        
        for(int i=0;i<S.size();i++)
        {
            if(S[i]>='A' && S[i]<='Z')
            {
                res+='Z'-S[i]+'A';
            }
            
            else if(S[i]>='a' && S[i]<='z')
            {
                res+='z'-S[i]+'a';
            }
            
            else
            {
                res+=S[i];
            }
        }
        
        return res;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    string S;
    cin>>t;
    cin.ignore();
    while(t--)
    {
        getline(cin,S);
        Solution ob;
        string reciprocal = ob.reciprocalString(S);
        cout<< reciprocal <<endl;

    }

	return 0;
}
// } Driver Code Ends