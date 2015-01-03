class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if (len(s1) != len(s2) or (len(s1) == 1 and s1[0] != s2[0])):
            return False;
        length = len(s1);
        scramble = [[[False for i in range(length)]for i in range(length)]for i in range(length+1)];
        #print (scramble);
        for i in range(length):
            for j in range(length):
                scramble[0][i][j] = True;
                scramble[1][i][j] = True if (s1[i] == s2[j]) else False;
                if (i< length-1 and j < length-1):
                    scramble[2][i][j] = True if ((s1[i] == s2[j]) and (s1[i+1] == s2[j+1])) or ((s1[i] == s2[j+1]) and (s1[i+1] == s2[j])) else False;

        for k in range(3, length+1):
            for i in range(length-k+1):
                for j in range(length-k+1):
                    for m in range(1, k):
                        check1 = scramble[m][i][j] and  scramble[k-m][i+m][j+m];
                        check2 = scramble[m][i][j+k-m] and  scramble[k-m][i+m][j];
                        canScramble = check1 or check2;
                        if (canScramble):
                            break;
                    scramble[k][i][j] = canScramble;

        
        #print (scramble);
        return scramble[length][0][0];

sol = Solution();
#sol.isScramble("abc","bac"); 
sol.isScramble("great", "ategr");