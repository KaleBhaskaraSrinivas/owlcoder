// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int N=1000001;
    int seive[1000001];
    void gen_seive()
    {
        seive[0]=0;
        seive[1]=0;
        for(int i=2;i<N;i++)
        {
            seive[i]=1;
        }
        for(int i=2;i*i<N;i++)
        {
            if(seive[i]==1)
            {
                for(int j=i*i;j<N;j+=i)
                {
                    seive[j]=0;
                }
            }
       }
    }
     vector<int>gen_primes(int num)
    {
        vector<int>d;
        for(int i=2;i<=num;i++)
        {
            if(seive[i]==1)
            {
                d.push_back(i);
            }
        }
        return d;
    }
    long long primeProduct(long long l, long long r){
       
        // code here
         gen_seive();
        vector<int>dj=gen_primes(sqrt(r)+1);
        vector<int>seg(r-l+1,1);
       
        for(auto it:dj){
            int first_mul=0;
            if((l/it)*it<l)
            {
                first_mul=((l/it)+1)*it;
            }
            else{
                first_mul=(l/it)*it;
            }
            for(int j=max(first_mul,it*it);j<=r;j+=it)
            {
                seg[j-l]=0;
            }
        }
        long long res=1;
        for(int i=0;i<r-l+1;i++)
        {
            if(seg[i]==1)
            {
                res=res*(l+i)%1000000007;
            }
        }
        return res%1000000007;
    }
};


// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        long long L, R;
        cin>>L>>R;
        
        Solution ob;
        cout<<ob.primeProduct(L, R)<<"\n";
    }
    return 0;
}  // } Driver Code Ends
