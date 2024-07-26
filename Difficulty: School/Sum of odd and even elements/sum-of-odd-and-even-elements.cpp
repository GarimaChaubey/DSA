//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
	public:
		vector<int> find_sum(int n)
		{
		int sum1=0;
        int sum2=0;
        vector<int>res;
        for(int i=0;i<=n;i++)
        {
            if(i%2==0)
            {
                sum2+=i;
            }
            else
            {
                sum1+=i;
            }
        }
        
        res.push_back(sum1);
        res.push_back(sum2);
        
        return res;
		}
};

//{ Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	int n;
    	cin >> n;
    	Solution ob;
    	vector<int> ans = ob.find_sum(n);
    	for(auto i: ans)
    		cout << i << " ";
    	cout<<"\n";
    }
	return 0;
}
// } Driver Code Ends