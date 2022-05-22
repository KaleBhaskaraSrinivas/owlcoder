class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        ans = ""
        pos = 0
        for i in range(Q):
            if index[i]>=pos:
                end=index[i]+len(sources[i])
                if sources[i] == S[index[i]:end]:
                    ans += S[pos:index[i]]+ targets[i]
                    pos = end
        return ans + S[pos:]
