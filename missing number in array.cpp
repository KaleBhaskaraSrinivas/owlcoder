class Solution{
  public:
    int MissingNumber(vector<int>& array, int n) {
        // Your code goes here
        int actual = (n*(n+1)/2);
             int total = 0;
               for(int num : array){
                   total += num;

               }
                     return actual- total;
    }
};
