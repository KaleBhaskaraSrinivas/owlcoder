class Solution{
   int count=0;
   int fun(int ind,vector<int>&arr,int n,int k,int sum)
   {
       if(ind==n)
       {
          if(sum==k)
           count++;
          return 0;
       }
     
       int pick=fun(ind+1,arr,n,k,(sum^arr[ind]));
       int not_pick=fun(ind+1,arr,n,k,sum);
       return pick+not_pick;
   }
public:
   int subsetXOR(vector<int> arr, int N, int K) {
       // code here
       int sum=0;
        fun(0,arr,N,K,sum);
       return count; 
       
   }
};
