#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
       st=[]
       ss=""
       for i in range(0,len(S)+1):
           st.append(i+1)
           if i==len(S) or S[i]=='I':
             while len(st):
                 ss+=str(st.pop());
       return int(ss)
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
