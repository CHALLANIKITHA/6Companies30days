#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    result=arr+" "
    string=""
    count=0
    ch=arr[0]
    for i in result:
        if i==ch:
            count+=1
        else:
            string+=str(ch)+str(count)
            ch=i
            count=1
    return string

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
