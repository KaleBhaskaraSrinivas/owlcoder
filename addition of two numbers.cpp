 // } Driver Code Ends
class Solution{   
public:
    int addition(int A, int B){
        int sum=0;
        sum=A+B;
        return sum;
        // code here 
    }
};

// { Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int A, B;
        cin >> A >> B;
        Solution ob;
        cout << ob.addition(A,B) << endl;
    }
    return 0; 
} 
  // } Driver Code Ends
