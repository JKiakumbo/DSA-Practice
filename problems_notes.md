# Problem Solving Template

## Problem Metadata
- **Name:** Two Sum
- **Link:** https://leetcode.com/problems/two-sum/
- **Difficulty:** [Easy/Medium/Hard]
- **Pattern:** Hash Map
- **Tags:** array, hash-table

## Key Dates
- **First Attempt:** 2024-01-15
- **Solved On:** 2024-01-15
- **Time Spent:** 20 minutes

## Solution
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

## Approach Steps
1. Create hash map to store numbers and their indices
2. For each number, calculate its complement (target - current)
3. Check if complement exists in hash map
4. If found, return both indices; otherwise store current number

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- HashMap allows O(1) lookups for complements
- Can solve in single pass instead of nested loops

### What Worked Well
- Immediately recognized HashMap pattern
- Handled edge cases correctly

### Challenges Faced
- Initially considered brute force O(n²) approach
- Remembered to store index after checking complement

### For Next Time
- Practice more HashMap variations
- Study two-pointer alternative approach

