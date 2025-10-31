# Product of Array Except Self

## Problem Metadata
- **Name:** Product of Array Except Self
- **Link:** https://algo.monster/problems/product_of_array_except_self
- **Difficulty:** Medium
- **Pattern:** Prefix Sum
- **Tags:** 

## Key Dates
- **First Attempt:** 30-10-2025
- **Solved On:** 30-10-2025

## Solution
```python
def product_of_array_except_self(nums: list[int]) -> list[int]:
    size = len(nums)
    ans = [1] * size

    left = 1
    for i in range(size):
        ans[i] = left
        left *= nums[i]

    right = 1
    for i in reversed(range(size)):
        ans[i] *= right
        right *= nums[i]

    return ans
```

## Approach Steps
1. Initialize an answer array `ans` of the same size as `nums`, filled with `1`s.
2. Create a variable `left` to keep track of the product of all elements to the left of the current index.
3. Loop through the array from left to right:
   - Set `ans[i]` to `left`.
   - Update `left` by multiplying it with `nums[i]`.
4. Create a variable `right` to keep track of the product of all elements to the right of the current index.
5. Loop through the array from right to left:
   - Multiply `ans[i]` by `right`.
   - Update `right` by multiplying it with `nums[i]`.
6. Return the `ans` array, which now contains the product of all elements except for the element at each index.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- The problem can be solved without using division by maintaining separate products for the left and right sides of each element.
- Two passes through the array (one from the left and one from the right) allow us to build the result efficiently.
- The approach ensures that we do not use extra space for left and right product arrays, keeping space complexity optimal.prefix-sum, array, range-sum-query

### What Worked Well
- Clear understanding of prefix sums and how to apply them to product calculations.
- Efficiently maintained left and right products with constant time updates.

### Challenges Faced
- Initially struggled with the concept of maintaining two separate products (left and right) without using extra space for them.
- Understanding the order of operations when updating the answer array.

### For Next Time
- Practice more problems involving prefix sums and product calculations to solidify understanding.
- Focus on edge cases, such as arrays with zeros or negative numbers.
