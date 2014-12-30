class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        lengthOfA = (len(A)-1);
        if (lengthOfA < 2):
            return 0;
        maxOnLeft = [A[0], A[0]];
        maxOnRight =[None] * (lengthOfA+1);
        maxOnRight[lengthOfA] = A[lengthOfA];
        maxOnRight[lengthOfA-1] = A[lengthOfA];
        for index in range(2, lengthOfA+1):
            maxOnLeft.append(maxOnLeft[index-1] if A[index-1] < maxOnLeft[index-1] else A[index-1]);
        index = lengthOfA-2;
        while (index >=0):
            maxOnRight[index] = (maxOnRight[index+1] if A[index+1] < maxOnRight[index+1] else A[index+1]);
            index = index -1;
        trappedWater = 0;
        index = 1;
        while(index < lengthOfA):
            minLevel = maxOnLeft[index] if maxOnLeft[index] < maxOnRight[index] else maxOnRight[index];
            trappedWater = trappedWater + (minLevel-A[index] if minLevel > A[index] else 0);
            index = index + 1;
        return trappedWater;

    #def trap(self, A):
    #    secH = 0;
    #    area = 0;
    #    left = 0;
    #    right = len(A) - 1;
    #    while (left < right):
    #        left_A = A[left];
    #        right_A = A[right];
    #        if (left_A < right_A):
    #            secH = left_A if (left_A > secH) else secH;
    #            area = area + secH - left_A;
    #            left = left + 1;
    #        else:
    #            secH = A[right] if (A[right] > secH) else secH;
    #            area = area + secH - A[right];
    #            right = right - 1;
        
    #    return area;

sol = Solution();
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]));