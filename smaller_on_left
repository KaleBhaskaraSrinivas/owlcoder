vector<int> Smallestonleft(int arr[], int n)
{
    // Complete the function
    set<int>s;
    vector<int>res;
    for(int i=0;i<n;i++){
    auto x=s.lower_bound(arr[i]);
    if(x==s.begin()){
        res.push_back(-1);
    }
    else{
        res.push_back(*--x);
    }
    s.insert(arr[i]);
}
return res;

}
