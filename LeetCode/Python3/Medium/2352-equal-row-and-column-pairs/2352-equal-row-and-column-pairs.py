from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0

        rows, cols = defaultdict(int), defaultdict(int)
        for i in range(len(grid)):
            rows[tuple(grid[i])] += 1
            
            col = [grid[j][i] for j in range(len(grid))]
            cols[tuple(col)] += 1

        for k in rows.keys():
            if k in cols:
                ans += rows[k] * cols[k]

        return ans