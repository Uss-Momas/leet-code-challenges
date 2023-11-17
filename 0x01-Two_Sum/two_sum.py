#!/usr/bin/python3
"""two_sum module"""
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
        """twoSum function 
        Args:
            - nums: list containing the numbers
            - targe: the target number to be verified
        """
        # first loop
        for i in range(1, len(nums)):
            # second loop
            for j in range(i, len(nums)):
                # sum the actual number and the next on the list
                sum = nums[i - 1] + nums[j]
                if sum == target:
                    return [i - 1, j]
