 void lnr(Node *root,vector<int>&v){
        if(root == NULL){
            return;
        }
        v.push_back(root->data);
        lnr(root->left,v);
        lnr(root->right,v);
    }
vector <int> preorder(Node* root)
{
   vector<int> v;  
  lnr(root,v);
  return v;
}
