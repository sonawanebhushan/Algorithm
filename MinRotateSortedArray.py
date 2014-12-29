class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        end = len(num) - 1;
        start = 0;
        while (1):
            mid = int((end + start)/2);
            if start+1 == end or start == end:
                break;
            if num[mid] < num[start]:
                end = mid;
            if num[mid] > num[end]:
                start = mid;
            else:
                end = mid;
        return num[start] if (start == end or (start+1==end and num[start] < num[end])) else num[end];

sol = Solution();
#print(sol.findMin([2,4,5,6,7,0,1]));
print(sol.findMin([3,4,5,1,2]));