vector<vector<int>> levelOrder(Node* root)
{
   vector<vector<int>>ans;
        if(root==NULL){
            return {};
        }
        queue<Node*>q;
        q.push(root);
        
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
        ans.push_back(row);
        }
        return ans;
}
