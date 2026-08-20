from collections import deque

class Solution:
    def numIslands(self, grid):

        n = len(grid)
        m = len(grid[0])

        vis = [[False] * m for _ in range(n)]

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        ans = 0

        for i in range(n):

            for j in range(m):

                if grid[i][j] == '1' and not vis[i][j]:

                    ans += 1

                    q = deque()
                    q.append((i,j))
                    vis[i][j] = True

                    while q:

                        r,c = q.popleft()

                        for dr,dc in directions:

                            nr = r + dr
                            nc = c + dc

                            if 0<=nr<n and 0<=nc<m and not vis[nr][nc] and grid[nr][nc]=='1':
                                vis[nr][nc]=True
                                q.append((nr,nc))

        return ans