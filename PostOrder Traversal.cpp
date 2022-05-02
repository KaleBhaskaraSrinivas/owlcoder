void lnr(Node *root,vector<int>&v){
        if(root == NULL){
            return;
        }
        
        lnr(root->left,v);
        lnr(root->right,v);
        v.push_back(root->data);
    }
vector <int> postOrder(Node* root)
{
  vector<int> v;  
  lnr(root,v);
  return v;
  
}
