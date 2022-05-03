class Solution{
    public:
    vector<int>ans;
   
    void Preorder(Node* root){
         if(root==NULL){
        return;
    }
        ans.push_back(root->data);
        Preorder(root->left);
        Preorder(root->right);
        
    }
    vector<int> preOrder(Node* root)
    {
        Preorder(root);
        return ans;
    }
};
