#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        for i in ransomNote:
            if(magazine.find(i)>=0):
                k=magazine.find(i)
                magazine = magazine[:k]+magazine[k+1:]
                c+=1
        if c==len(ransomNote):
            return True
        else:
            return False
                
    def main():
        ransomNote = input()
        magazine = input()
        note = canConstruct(ransomNote,magazine)
        print(note)
        
