class Solution
{
    public:

    int sumtree(Node* root){
        if(root==NULL){
            return 0;
        }
        if(root->left==NULL and root->right==NULL){
            return root->data;
        }
        
        int lsum = sumtree(root->left);
        int rsum = sumtree(root->right);
        
        if(root->data != (lsum + rsum)){
            return 0;
        }
        return lsum+rsum+root->data;
    }
    
    bool isSumTree(Node* root)
    {
         // Your code here
         return(sumtree(root));
    }
};
