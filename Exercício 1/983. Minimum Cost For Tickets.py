from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        last_day = days[-1]
        
        dp = [0] * (last_day + 1)
        
        for day in range(1, last_day + 1):
            if day not in day_set:
                dp[day] = dp[day - 1]
            else:
                cost1 = dp[day - 1] + costs[0]
                cost7 = dp[max(0, day - 7)] + costs[1]
                cost30 = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(cost1, cost7, cost30)
        
        return dp[last_day]
