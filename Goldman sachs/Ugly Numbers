#User function Template for python3
class Solution:
    def getNthUglyNo(self,n):
        # code here
        c1,c2,c3=0,0,0
        x=[0]*(n+1)
        x[0]=1
        for i in range(1,n+1):
            x[i]=min(2*x[c1],3*x[c2],5*x[c3])
            if 2*x[c1]==x[i]:
                c1+=1
            if 3*x[c2]==x[i]:
                c2+=1
            if 5*x[c3]==x[i]:
                c3+=1
        return x[n-1]
          
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends
