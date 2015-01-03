#class Solution:
#    # @param prices, a list of integer
#    # @return an integer
#    def maxProfit(self, prices):
#        if (len(prices) == 0 or len(prices) == 1):
#            return 0;
#        index = 1;
#        totalProfit = 0;
#        for index in range(1, len(prices)):
#             if (prices[index-1] < prices[index]):
#                totalProfit = totalProfit + prices[index]-prices[index-1];
#        return totalProfit;

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        currIndex = 0
        jumps = 1
        if (len(A) == 1 or len(A) == 0):
            return 0;
        while ((A[currIndex]) < (len(A)-currIndex-1)):
            max = 0
            maxIndex = currIndex
            value = A[currIndex]
            for i in range(currIndex+1, (currIndex + value+1)):
                if (max < A[i] + i-currIndex):
                    max = A[i] + i-currIndex
                    maxIndex = i
            currIndex = maxIndex
            jumps += 1
        
        return jumps
            
sol = Solution();
#print(sol.jump([5,9,3,2,1,0,2,3,3,1,0,0]));
print(sol.jump([0,0,0,0,0,0]));
