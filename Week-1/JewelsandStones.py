#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        l1 = list(J)
        l2 = list(S)
        count = 0
        for i in l2:
            if i in l1:
                count+=1
        return count
    def main():
        J = input()
        S = input()
        jewels = numJewelsInStones(J,S)
        print(jewels)
