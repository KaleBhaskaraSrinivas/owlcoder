class Solution
{
public:
    void FindSubSetSum(int ind, int sum,int N,vector<int> &arr, vector<int>&ans)
    {
        if(ind==N){
            ans.push_back(sum);
            return;
        }
        sum+=arr[ind];
        FindSubSetSum(ind+1,sum,N,arr,ans);
        sum-=arr[ind];
        FindSubSetSum(ind+1,sum,N,arr,ans);
    }
    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int>ans;
        FindSubSetSum(0,0,N,arr,ans);
        return ans;
        
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}  // } Driver Code Ends
