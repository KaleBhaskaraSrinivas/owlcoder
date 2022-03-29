#include<math.h>
using namespace std;
int findIndex(int arr[], int X, int Y, int n);


int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	while(t--)
	{
		int n,x,y;
		cin>>n>>x>>y;
		int a[n];
		for(int i=0;i<n;++i)
			cin>>a[i];
		cout<<findIndex(a,x,y,n)<<endl;
	}
	return 0;
}
// } Driver Code Ends



int findIndex(int arr[], int X, int Y, int N)
{
    // Your code goes here
    int index=-1;
    int x=0;
    int y=0;
    int maxi=-1;
    for(int i=0;i<N;i++){
        if(arr[i]==X){
            x++;
        }else if(arr[i]==Y)
        {
            y++;
        }
        if(x==y && x>0 && y>0){
            maxi=max(maxi,i);
        }
    }
    
    return maxi;
} 
