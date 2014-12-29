class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if (len(num) < 2):
            return 0;
        max = num[0];
        min = num[0];
        for number in num:
            if (max < number):
                max = number;
            if (min > number):
                min = number;
        bucketsize = float(float(max-min)/float(len(num)-1));
        maxarray = [];
        minarray = [];
        for index in range(0, len(num)-1):
            maxarray.append(-1);
            minarray.append(-1);

        for number in num:
            index = ((len(num)-2) if (number == max) else (int((number-min)/bucketsize)));
            if (minarray[index] == -1 or number < minarray[index]):
                minarray[index] = number;
            if (maxarray[index] == -1 or number > maxarray[index]):
                maxarray[index] = number;

        preMax = maxarray[0];
        maxGap = maxarray[0] - minarray[0];
        for index in range(0, len(maxarray)):
            if (minarray[index] == -1):
                continue;
            if (maxGap < (minarray[index] - preMax)):
                maxGap = (minarray[index] - preMax);
            preMax = maxarray[index];
        return maxGap;


sol = Solution();
print(sol.maximumGap([1,1,1,1,1,5,5,5,5,5]));