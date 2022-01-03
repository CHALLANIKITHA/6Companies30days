class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minwindowsize=float('inf')
        currentwindowsum=0
        windowstart=0
        for windowend in range(0,len(nums)):
            currentwindowsum+=nums[windowend]
            while currentwindowsum>=target:
                minwindowsize=min(minwindowsize,windowend-windowstart+1)
                currentwindowsum-=nums[windowstart]
                windowstart+=1
        if minwindowsize!=float('inf'):
               return minwindowsize
        else:
            return 0
