'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''



#MY APPROACH
'''
 class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r_arr = []
        currSum = 0
        for i in range(len(nums)):
            currSum = currSum +nums[i]
            if currSum <0:
                r_arr.append(currSum)
                n_arr = nums[i:]
                val = self.maxSubArray(n_arr)
            r_arr.append(currSum)
        r_arr.append(currSum)
        res = max(r_arr)
        return res

 
 
 
 '''



#Correct approach


class Solution(object):
    def maxSubArray(self, nums):
        best_end = best = nums[0]
        for x in nums[1:]:
            best_end = max(x, best_end + x)
            best = max(best, best_end)
        return best
    
    