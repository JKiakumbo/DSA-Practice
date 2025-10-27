# **Coding Pattern Notes**

**Pattern Name:** Prefix Sum
**Status:** Learning
**Date Started:** 27.10.2025
**Date Mastered:** [Date]

---

## **1. 🧠 Pattern Overview**

* **Core Concept:** The prefix sum is an incredibly powerful and straightforward technique. Its primary goal is to allow for constant-time range sum queries on an array.
    The prefix sum of an array at index 'i' is the sum of all numbers from index '0' to 'i'. By computing and storing the prefix sum of an array, you can easily answer queries about the sum of any subarray in constant time. 

* **When to Use (Key Signals):**
    * Signal 1: Problems that require frequent sum calculations over subarrays or ranges.
    * Signal 2: Problems that involve cumulative sums or need to find sums of contiguous segments.
    * Signal 3: Problems that can be optimized from O(n^2) to O(n) by precomputing sums.
* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## **2. 📝 The Universal Template**

*(This is the most important section. Keep the code clean and commented.)*
```python
def build_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum

# Query sum of range [left, right] (inclusive)
def query_range(prefix_sum, left, right):
    if left == 0:
        return prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left-1]


```
**Template Breakdown & Notes:**
* **Building Prefix Sum Array:** The `build_prefix_sum` function constructs the prefix sum array in O(n) time. Each element at index 'i' in the prefix sum array is the sum of all elements from index '0' to 'i' in the original array.
* **Range Sum Query:** The `query_range` function allows for O(1) time range sum queries. If the left index is '0', it simply returns the prefix sum at the right index. Otherwise, it subtracts the prefix sum at 'left-1' from the prefix sum at 'right' to get the sum of the subarray from 'left' to 'right'.
* **Return Value:** The return value of the `query_range` function is the sum of the elements in the specified range.
---

## **3. 🔄 Variations & Common Tricks**
* **Variations:**
    * **2D Prefix Sum:** Extend the concept to two-dimensional arrays for submatrix sum queries.
    * **Prefix Product:** Similar to prefix sum, but for products instead of sums.
    * **Modular Prefix Sum:** Useful in problems involving large numbers where results need to be taken modulo a certain value.
* **Common Pitfalls:**
    * Forgetting to handle edge cases, such as empty arrays or invalid indices.
    * Misunderstanding the inclusive/exclusive nature of range queries.
    * Not initializing the prefix sum array correctly, leading to off-by-one errors.
---

## **4. ✅ Solved Problems Log**

*(For each problem you solve, add a quick entry. Focus on the insight, not the code.)*

| Problem Name                                                                                          | Difficulty | Key Insight & Why This Pattern                                     | Edge Cases                         | Date Solved |
|:------------------------------------------------------------------------------------------------------|:-----------|:-------------------------------------------------------------------|:-----------------------------------|:------------|
| [Find the First True in a Sorted Boolean Array](https://algo.monster/problems/binary_search_boundary) | Easy       | Classic template application. Array is sorted, need O(log n) time. | Single element, target not present | 23-09-2025  |

---

## **5. 📚 Resources & Links**
* **AlgoMonster Concept Link:** [Prefix Sum](https://algo.monster/problems/subarray_sum)
