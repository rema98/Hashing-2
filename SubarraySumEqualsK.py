# Problem: Subarray Sum Equals K (LeetCode 560)
# Time Complexity: O(n), where n = len(nums)
# Space Complexity: O(n), due to the hashmap storing up to n prefix sums.
# Implementation Thought: Use a running prefix sum and hashmap to count how many times each prefix sum appears.

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # Base case: one way to have sum = 0 before starting
        
        for num in nums:
            current_sum += num
            # If (current_sum - k) has appeared before, any subarray ending here summing to k contributes that many times.
            if (current_sum - k) in prefix_counts:
                count += prefix_counts[current_sum - k]
            # Record the current prefix sum occurrence
            prefix_counts[current_sum] += 1

        return count
