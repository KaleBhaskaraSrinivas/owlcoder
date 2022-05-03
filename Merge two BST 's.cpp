class Solution
{
    public:
    void inorder(Node *root,vector<int>&ans){
       if(root==NULL){
           return;
       }
       inorder(root->left,ans);
       ans.push_back(root->data);
       inorder(root->right,ans);
   }
    //Function to return a list of integers denoting the node 
    //values of both the BST in a sorted order.
    vector<int> merge(Node *root1, Node *root2)
    {
        vector<int>v;
      if(root1==NULL and root2==NULL){
          return v;
      }
      inorder(root1,v);
      inorder(root2,v);
      sort(v.begin(),v.end());
      return v;
    }
};
