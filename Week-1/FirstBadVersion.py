#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

class Solution:
    def firstBadVersion(self, n):
        return self.bs(0,n)

    def nw(self,s,e):
        if e==s:
            return e
        mid=s+ (e-s)//2
        cur=isBadVersion(mid)    
        if cur==True:
            return self.nw(s,mid)
        if cur==False:
            return self.nw(mid+1,e)
