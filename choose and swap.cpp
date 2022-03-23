#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
public:
    string chooseandswap(string a){
        // Code Here
        set<char>st;
        int l=a.length();
        for(int i=0;i<l;i++){
            st.insert(a[i]);
        }
        for(int i=0;i<l;i++){
            st.erase(a[i]);
            if(st.size()==0){
                break;
            }
            char ch=*st.begin();
            if(a[i]>ch){
                char ch2=a[i];
                for(int j=0;j<l;j++){
                    if(a[j]==ch){
                        a[j]=ch2;
                    }
                    else if(a[j]==ch2){
                        a[j]=ch;
                    }
                }
                break;
            }
        }
        return a;
    }
};


// { Driver Code Starts.

int main()
{
    Solution obj;
	int t;
	cin >> t;
	while(t--)
	{	
	    string a;
		cin >> a;
		cout << obj.chooseandswap(a) << endl;
	}
	return 0;
}
  // } Driver Code Ends
