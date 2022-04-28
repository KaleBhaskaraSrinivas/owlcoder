class Solution{
    int minEle;
    stack<int> s,ss;
    public:
    
       /*returns min element from stack*/
       int getMin(){
           if(ss.size()==0){
               return -1;
           }
           return ss.top();
       }
       
       /*returns poped element from stack*/
       int pop(){
           if(s.size()==0){
               return -1;
           }
           int ans=s.top();
           s.pop();
           if(ans==ss.top()){
               ss.pop();
           }
           return ans;
       }
       
       /*push element x into the stack*/
       void push(int x){
           s.push(x);
           if(ss.size()==0 or x<=ss.top()){
               ss.push(x);
           }
       }
};





class Solution{
    int minEle;
    stack<int> s;
    public:
       /*returns min element from stack*/
       int getMin(){
           if(s.empty())
           {
           return -1;
               
           }
           else
           {
           return minEle;
           }
       }
       /*returns poped element from stack*/
       int pop(){
             int x;
          if (s.empty())
             return -1;
          int result = s.top();
          if (result < minEle) 
          {
              result = minEle;
              minEle = 2*minEle - s.top();
          }
          s.pop();
          return result;
       }
       
       /*push element x into the stack*/
       void push(int x){
            if (s.empty())
            {
              minEle = x;
              s.push(x);
            }
          else
          {
             if (x > minEle) 
             {
                  s.push (x);
             } else 
             {
                  s.push (2*x - minEle);
                  minEle = x;
             }
          }
       }
};
