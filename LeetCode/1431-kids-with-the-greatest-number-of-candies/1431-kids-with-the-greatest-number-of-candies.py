import numpy as np
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return ((np.array(candies) + extraCandies) >= np.max(candies)).tolist()