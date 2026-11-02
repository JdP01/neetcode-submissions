class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minbuy = prices[0]
        maxprofit = 0 

        for i in prices: 

            if i < minbuy: 
                minbuy = i

            if i - minbuy > maxprofit: 
                maxprofit = i - minbuy

        return maxprofit