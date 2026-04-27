class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buymin=prices[0]
        maxprofit=0
        for i in prices:
            buymin=min(buymin,i)
            profit=i-buymin
            maxprofit=max(maxprofit,profit)

        if maxprofit>0:
         return maxprofit
        else:
         return 0
    





      

        