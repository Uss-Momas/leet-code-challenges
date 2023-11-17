# 0x01 - Two Sum Problem
**Difficult - Easy**
## Problem statement
Given an array of integers **nums** and an integer **target**, return $$indices of the two numbers$$ such that they add up to **target**.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```


Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
 

## My Approach for the solution
### Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
At first I didnt understand very well the problem until I saw a test case that failed.
But after understanding the problem statement It became more/less clear to me.
So I started to sketch at my book the iteration for each element in the array, and it became clear to me that I had to walk through each of the next numbers from the starting point.

### Approach
<!-- Describe your approach to solving the problem. -->
My approach is simple:

1. First go through each index of the array starting from the next position, so that u dont get a index out of bound problem
2. Secondly, go through a second loop, at which we sum up the actual number from the first loop and the next(s) numbers from the list
3. Then put a condition to verify if the sum is the target, if it's just return the indexes in a new list.

### Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
    O(n^2)
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
    O(1)
### Code
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(i, len(nums)):
                sum = nums[i - 1] + nums[j]
                if sum == target:
                    return [i - 1, j]
                
        
```
