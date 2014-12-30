#Palindrome Partitioning II
#Given a string s, partition s such that every substring of the partition is a palindrome.

#Return the minimum cuts needed for a palindrome partitioning of s.

#For example, given s = "aab",
#Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut. 

import datetime
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        palindrome = [[False for x in range(len(s))] for x in range(len(s))];
        palindrome[0][0] = True;
        minCutSoFar = [x for x in range(len(s))];
        j = len(s)-1;
        #print (datetime.datetime.now());
        for i in range(len(s)):
            for j in range(len(s)):
                if (i<j):
                    continue;
                if (i==j):
                    palindrome[j][i] = True;
                elif(i>j):
                    palindrome[j][i] = True if(s[i] == s[j] and ((i-j == 1) or (j < len(s)-1 and palindrome[j+1][i-1]))) else False;

                if (i >= j):
                    if (palindrome[j][i] == True):
                        prevmincut = (((minCutSoFar[j-1]+1) if j > 0 else 0));
                        minCutSoFar[i] = prevmincut if (prevmincut < minCutSoFar[i]) else minCutSoFar[i];
                    else:
                        prevmincut = (minCutSoFar[j]+(i-j));
                        minCutSoFar[i] = (prevmincut) if (prevmincut < minCutSoFar[i]) else minCutSoFar[i];
        print (minCutSoFar);
        return minCutSoFar[len(s)-1]

sol = Solution();
#sol.minCut("aba");
#sol.minCut("abacabadabac");
print (datetime.datetime.now());
result = sol.minCut("bb");
#result = sol.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
print (datetime.datetime.now());
print (result);
#sol.minCut("abaca");

        
        #while (j >= 0):
        #    i = len(s)-1;
        #    while (i >= 0):
        #        if(i<j):
        #            check1 = True if j-i < 2  else False;
        #            check2 = True if palindrome[i+1][j-1] == True else False;
        #            palindrome[i][j] = True if (s[i] == s[j] and (check1 or check2)) else False;
        #            if (palindrome[i][j] == True):
        #                prevMinCut = (((minCutSoFar[j+1]+1) if j < len(s) else 0));
        #                minCutSoFar[i] = prevMinCut if (prevMinCut < minCutSoFar[i]) else minCutSoFar[i];
        #            else:
        #                prevMinCut = (minCutSoFar[j]+(j-i));
        #                minCutSoFar[i] = (prevMinCut) if (prevMinCut < minCutSoFar[i]) else minCutSoFar[i];
        #        elif (i==j):
        #            palindrome[i][j] = True;
        #        i = i -1;
        #    j = j -1;
        #print (palindrome);
                    
