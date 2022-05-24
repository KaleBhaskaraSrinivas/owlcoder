from collections import deque
class Solution:
    def partitionArray(self,N,K,M,arr):
        arr.sort()
        q = deque([0])
        for i in range(K-1,N):
            while i - q[0] + 1>=K:
                if arr[i] - arr[q[0]] <=M:
                    q.append(i+1)
                    break
                q.popleft()
                if not q:
                    return False
        return q[-1] == N
