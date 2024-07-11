//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
        string modify (string s)
        {
            string vow;
            
            for(char c : s)
            {
                if(c=='a'|| c=='e' || c=='i' || c=='o' || c=='u')
                {
                    vow+=c;
                }
            }
            
            int vowIndex = vow.length() - 1;
            //return vow;
            
            for (int i = 0; i < s.length(); i++) 
            {
                if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') 
                {
                    s[i] = vow[vowIndex--];
                }
            }
        return s;
        }
};

//{ Driver Code Starts.

int main()
{
    int t; cin >> t;
    while (t--)
    {
        string s; cin >> s;
        Solution ob;
        cout <<ob.modify (s) << endl;
    }
}
// Contributed By: Pranay Bansal

// } Driver Code Ends