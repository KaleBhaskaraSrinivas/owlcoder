class Solution
{
    public:
    //Function to return the level order traversal of a tree.
    vector<int> levelOrder(Node* root)
    {
        if(root==NULL){
            return {};
        }
        queue<Node*>q;
        q.push(root);
    vector<int>ans;    
    while(!q.empty()){
        Node* root=q.front();
        q.pop();
        ans.push_back(root->data);
        if(root->left){
            q.push(root->left);
        }
        if(root->right){
            q.push(root->right);
        }
        }
        return ans;
    }
};
