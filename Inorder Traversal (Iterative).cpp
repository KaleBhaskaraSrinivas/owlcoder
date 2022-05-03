class Solution {
public:
    vector<int>ans;
    void Inorder(Node* root){
      if(root==NULL){
          return;
      }
      Inorder(root->left);
      ans.push_back(root->data);
      Inorder(root->right);
    }

    vector<int> inOrder(Node* root)
    {
       Inorder(root);
       return ans;
    }
};
