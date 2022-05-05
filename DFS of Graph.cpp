class Solution {
  public:
    // Function to return a list containing the DFS traversal of the graph.
     void dfs(int i,vector<int>&vis,vector<int>&store,vector<int>adj[]){
      store.push_back(i);
      vis[i]=1;
      for(auto it: adj[i]){
          if(vis[it]==0){
              dfs(it,vis,store,adj);
          }
      }
  }
    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
        vector<int>store;
        vector<int>vis(V,0);
        for(int i=0;i<V;i++){
            if(vis[i]==0){
                dfs(i,vis,store,adj);
            }
        }
        return store;
    }
};
