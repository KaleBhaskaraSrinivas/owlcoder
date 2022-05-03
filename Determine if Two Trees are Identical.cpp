class Solution
{
    public:
    //Function to check if two trees are identical.
    bool isIdentical(Node *root1, Node *root2)
{
    if(root1 == NULL and root2 == NULL)
    {
        return true;
    }
    else if(root1 == NULL and root2 != NULL)
    {
        return false;
    }
    else if(root1 != NULL and root2 == NULL)
    {
        return false;
    }
    
    bool check1 = isIdentical(root1->left, root2->left);
    bool check2 = isIdentical(root1->right, root2->right);
    bool check3 = root1->data == root2->data;
    
    return check1 and check2 and check3;
}
};
