class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        z=[0]*(len(s)+1)
        z[0]=1
        if s[0]=='0':
            z[1]=0
        else:
            z[1]=1
        for i in range(2,len(s)+1):
            x=int(s[i-1:i])
            y=(int(s[i-2:i]))
            if x>0:
                z[i]+=z[i-1]
            if y<=26 and y>=10:
                z[i]+=z[i-2]
        return z[len(s)]
        
