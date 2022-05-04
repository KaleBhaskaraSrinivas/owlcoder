class Solution{
    public:
    //Function to store the zig zag order traversal of tree in a list.
    vector <int> zigZagTraversal(Node* root)
    {
    	if(root==NULL){
            return {};
        }
        queue<Node*>q;
        q.push(root);
        int flag=1;
    vector<int>ans;    
    while(!q.empty()){
        int size=q.size();
        vector<int>row(size);
         for(int i=0;i<size;i++){
            root=q.front();
            q.pop();
            row[i]=(root->data);
        
        if(root->left){
            q.push(root->left);
        }
        if(root->right){
            q.push(root->right);
        }
         }
       if(flag==1){
                for(int i=0;i<row.size();i++){
                    ans.push_back(row[i]);
                }
                flag=0;
            }
            else if(flag==0){
                for(int i=row.size()-1;i>=0;i--){
                    ans.push_back(row[i]);
                }
                flag=1;
            }
        }
    
        return ans;// Code here
}
};
