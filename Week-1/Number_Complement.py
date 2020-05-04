#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

import math
class Solution:
    def findComplement(self, num: int) -> int:
        number_of_bits = (int)(math.floor(math.log(num) / math.log(2))) + 1;
        
        return ((1<<number_of_bits)-1)^num;
    def main():
        num = int(input())
        print(findComplement(num))
        
