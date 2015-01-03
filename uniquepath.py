class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        uniquePath = [[0 for x in range(0,n)] for x in range(0,m)];
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    uniquePath[i][j] = 1;
                else:
                    uniquePath[i][j] = uniquePath[i-1][j] + uniquePath[i][j-1];
        return (uniquePath[m-1][n-1]);

sol = Solution();
print(sol.uniquePaths(3,7));