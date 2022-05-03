class Solution{
    public:
    bool f=true;
    int height(Node *root){
        if(root==NULL){
            return 0;
        }
        int l = height(root->left);
        int r = height(root->right);
        if(abs(l - r) > 1){
          f = false;  
        } 
        return max(l, r) + 1;
    }
    //Function to check whether a binary tree is balanced or not.
    bool isBalanced(Node *root)
    {
        height(root);
       return f; //  Your Code here
    }
};
