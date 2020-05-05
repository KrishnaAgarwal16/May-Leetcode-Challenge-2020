class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_ = list(set(s))
        s_.sort()
        min_=len(s)-1
        l=[]
        c=0
        if len(s)==1:
            return 0
        else:
            for i in s_:
                if s.count(i)==1:
                    if (s.find(i)<=min_):
                        min_ = s.find(i)
                        l.append(min_)
                        c+=1
            l.sort()
            if c!=0:
                return l[0]
            else:
                return -1
    def main():
        s = input()
        print(firstUniqChar(s))
