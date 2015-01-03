#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxProfit = 0;
        prevMin = None;
        currMinSoFar = None;
        for index in range(1, len(prices)):
            if (prevMin == None and prices[index-1] < prices[index]):
                currMinSoFar  = prices[index-1];
            if (prevMin != None and prices[index] > prevMin):
                currMinSoFar = prevMin;
            if (prevMin != None and prices[index-1] < prevMin):
                currMinSoFar = prices[index-1];
            priseForTodaysSell = (prices[index] - currMinSoFar) if (currMinSoFar != None and prices[index]>currMinSoFar) else 0;
            maxProfit =  max(maxProfit,priseForTodaysSell);
            prevMin = currMinSoFar;
        return maxProfit;

sol = Solution();
result = sol.maxProfit([2,1,2,1,0,1,2]);
print (result);

