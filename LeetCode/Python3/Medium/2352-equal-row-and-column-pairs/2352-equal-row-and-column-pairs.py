from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0

        rows, cols = defaultdict(int), defaultdict(int)
        for i in range(len(grid)):
            rows[tuple(grid[i])] += 1
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cols[tuple(col)] += 1

        print(rows)
        print(cols)

        for k in rows.keys():
            if k in cols:
                ans += rows[k] * cols[k]

        return ans