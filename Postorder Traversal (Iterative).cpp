class Solution{
    public:
    vector<int>ans;
   
    void Postorder(Node* node){
         if(node==NULL){
        return;
    }
        
        Postorder(node->left);
        Postorder(node->right);
        ans.push_back(node->data);
        
    }
    vector<int> postOrder(Node* node) {
        // code here
        Postorder(node);
        return ans;
    }
};
