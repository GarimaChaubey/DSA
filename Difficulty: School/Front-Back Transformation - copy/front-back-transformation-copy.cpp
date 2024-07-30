//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
string convert(string a);
int main()
{
    int t;
    cin>>t;
    while(t--)
        {
            string s;
            cin>>s;
            string ans=convert(s);
            cout<<ans<<endl;
            
        }
}

// } Driver Code Ends


string convert(string s)
{
    // code here.
    
    string res;
    
    for(char c:s)
    {
        int i=int(c);
        
        if(i>=65 && i<=90)
        {
            res+=char(65+90-i);
        }
        
        else if(i>=97 && i<=122)
        {
            res+=char(97+122-i);
        }
    }
    
    return res;
}