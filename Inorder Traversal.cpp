class Solution {
  public:
  vector<int> v;
    void lnr(Node *root){
        if(root == NULL){
            return;
        }
        lnr(root->left);
        v.push_back(root->data);
        lnr(root->right);
    }
    // Function to return a list containing the inorder traversal of the tree.
    vector<int> inOrder(Node* root) {
        // Your code here
        lnr(root);
        return v;
    }
};
