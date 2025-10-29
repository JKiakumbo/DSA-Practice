# Subarray Sum

## Problem Metadata
- **Name:** Subarray Sum
- **Link:** https://algo.monster/problems/subarray_sum
- **Difficulty:** Medium
- **Pattern:** Prefix Sum
- **Tags:** prefix-sum, array, subarray-sum

## Key Dates
- **First Attempt:** 27-10-2025
- **Solved On:** 29-10-2025

## Solution
```python
def subarray_sum(arr: list[int], target: int) -> list[int]:
    # prefix_sum 0 happens when we have an empty array
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1
    return []


# Follow-up Problem
from collections import Counter

def subarray_sum_total(arr: list[int], target: int) -> int:
    prefix_sums: Counter[int] = Counter()
    prefix_sums[0] = 1  # since empty array's sum is 0
    cur_sum = 0
    count = 0
    for val in arr:
        cur_sum += val
        complement = cur_sum - target
        if complement in prefix_sums:
            count += prefix_sums[complement]
        prefix_sums[cur_sum] += 1
    return count
```

## Approach Steps
1. Initialize a dictionary `prefix_sums` to store the cumulative sums and their corresponding indices, starting with the sum `0` at index `0`.
2. Initialize a variable `cur_sum` to keep track of the current cumulative sum as we iterate through the array.
3. Loop through each element in the array:
   - Update `cur_sum` by adding the current element.
   - Calculate the `complement` as `cur_sum - target`.
   - Check if `complement` exists in `prefix_sums`:
     - If it does, return the starting and ending indices of the subarray that sums to the target.
   - If not, store the current `cur_sum` with its index in `prefix_sums`.
4. If no subarray is found that sums to the target, return an empty list.
5. For the follow-up problem, use a `Counter` to keep track of the frequency of each prefix sum and count the number of valid subarrays that sum to the target.


## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- Prefix sums can be used to efficiently find subarrays with a given sum.
- Storing cumulative sums in a hash map allows for O(1) lookups to find complements.
- The follow-up problem can be solved by counting occurrences of prefix sums using a Counter.


### What Worked Well
- Clear understanding of prefix sum technique.
- Efficiently tracked cumulative sums and their indices.

### Challenges Faced
- Understanding the need to store prefix sums and their frequencies for the follow-up problem.
- Understanding how to count multiple subarrays that sum to the target.
- Understanding the need of dictionary to store prefix sums for quick lookup.

### For Next Time
- Practice more problems involving prefix sums and subarray sums.
- Review edge cases for subarray sum problems.
