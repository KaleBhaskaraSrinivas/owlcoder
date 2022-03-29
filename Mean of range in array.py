#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
    public:
     vector<int> findMean(int arr[],int queries[],int n,int q)
    {
        for(int i=1; i<n; i++)
            arr[i] += arr[i-1];
        vector <int> res;
        int j = 0;
        q /= 2;
        while(q--){
            int l = queries[j];
            int r = queries[j+1];
            if(l == 0)
                res.push_back(arr[r]/(r+1));
            else
                res.push_back((arr[r]-arr[l-1])/(r-l+1));
            j += 2;
        }
        return res;
    }

};

// { Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        cin>>n>>q;
        int arr[n + 1],queries[2*q + 1];

        for(int i=0;i<n;i++){
            cin>>arr[i];
        }

        for(int i=0;i<2*q;i++){
            cin>>queries[i];
        }

        vector<int> ans;
        Solution ob;
        ans = ob.findMean(arr,queries,n,2*q);

        for(int i:ans)
            cout<<i<<" ";
        cout<<endl;

    }
    return 0;
}
  // } Driver Code Ends
