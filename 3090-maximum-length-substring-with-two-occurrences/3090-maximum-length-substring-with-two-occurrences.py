class Solution:
    def maximumLengthSubstring(self,s):
        c={};l=a=0
        for r,x in enumerate(s):
            c[x]=c.get(x,0)+1
            while c[x]>2:c[s[l]]-=1;l+=1
            a=max(a,r-l+1)
        return a