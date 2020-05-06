#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = set(nums)
        n = len(nums)
        for i in d:
            if nums.count(i)>(n/2):
                return i
            
    def main():
        nums = list(map(int(input())))
        print(majorityElement(nums))
