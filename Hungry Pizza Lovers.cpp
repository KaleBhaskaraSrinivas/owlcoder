vector<int> permute(vector<vector<int>> &arr, int n)
{
    
    // Complete the function
    for(int i=0;i<arr.size();i++){
        arr[i][0]=arr[i][0]+arr[i][1];
        arr[i][1]=i+1;
    }
    sort(arr.begin(),arr.end());
    vector<int>ans;
    for(int i=0;i<arr.size();i++){
        ans.push_back(arr[i][1]);
    }
    return ans;
    
}
