#User function Template for python3
from itertools import permutations
from itertools import combinations
class Solution:
    def canPair(self, nums, k):
        # Code here
       m=dict()
       for i in range(0,k):
           m[i]=0
       n=len(nums)
       for i in range(0,len(nums)):
           m[nums[i]%k]+=1
       for i in range(0,n):
           r=nums[i]%k
           if r==0 :
               if m[0]&1:return 0
           elif(m[r]!=m[k-r]):return 0
       return 1
       

        
    
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
# } Driver Code Ends
