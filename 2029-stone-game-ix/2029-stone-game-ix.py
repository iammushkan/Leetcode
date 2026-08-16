class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = [0, 0, 0]
        for s in stones:
            c[s % 3] += 1
            
        zero_is_even = (c[0] % 2 == 0)
        
        if zero_is_even:
            return c[1] > 0 and c[2] > 0
        
        diff = abs(c[1] - c[2])
        return diff > 2