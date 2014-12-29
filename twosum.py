class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {};
        print 'two sum!';
        for index in range(0, len(num)):
            dict [num[index]] = index;

        for index in range (0, len(num)):
            if (dict.has_key(target - num[index])) and (index <> dict[target - num[index]]):
                break;
        print 'found indexes!';
        print index+1;
        print dict[target-num[index]]+1;
        print 'numbers';
        print num[index];
        print target-num[index];
        return (index+1, dict[target-num[index]]+1);

solution = Solution();
solution.twoSum( 	[3,2,4], 6);
print 'Test!';