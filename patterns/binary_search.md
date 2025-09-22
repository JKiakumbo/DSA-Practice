# **Coding Pattern Notes**
**Pattern Name:** Binary Search
**Status:** Learning
**Date Started:** 22.09.2025
**Date Mastered:** [Date]

---

## **1. 🧠 Pattern Overview**
*   **Core Concept:** Binary Search is an efficient array searching algorithm.
It works by repeatedly dividing the search interval(limited by left and right pointers) in half to find the target quicker.
The idea is to find the middle element and compare it with the target value.
If they are not equal, the half in which the target cannot lie is eliminated,
and the search continues on the remaining half until the target is found or the interval is empty.
*   **When to Use (Key Signals):**
    *   Signal 1: The input array is sorted, or we make a binary decision to reduce the search range.
    *   Signal 2: Problem requires O(log n) time complexity
*   **Time Complexity:** O(log n)
*   **Space Complexity:** O(1)

---

## **2. 📝 The Universal Template**
*(This is the most important section. Keep the code clean and commented.)*

```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1  #First true index
    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow for Python mid = (left + right) // 2 is okay
        if feasible(mid):
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index
```
**Template Breakdown & Notes:**
*   **Loop Condition:** We use `while left <= right` to ensure we check all elements, including when left is equals right.
*   **Mid Calculation:** `left + (right - left) // 2` is safer than `(left+right)//2` because it prevents potential overflow in languages with fixed integer sizes.
*   **The Condition Function:** This is the key to adapting the template. It defines what we are searching for. In this case, `feasible(mid)` checks if the mid element meets the criteria (e.g., `arr[mid] >= target` for finding the first occurrence of target).
*   **Return Value:** We return `boundary_index`, which is the index of the first occurrence of the target if found, otherwise -1.

---

## **3. 🔄 Variations & Common Tricks**
*   **Variation 1: Finding an Exact Match**
    *   `Condition:` `array[mid] == target` -> then return `mid`.
*   **Variation 2: Finding the First Occurrence**
    *   `Condition:` `array[mid] >= target` -> then return `left`.
*   **Variation 3: Search in a Rotated Sorted Array**
    *   Insight: One half of the array will always be sorted. Check which half and adjust pointers accordingly.
*   **Common Pitfalls:**
    *   Off-by-one errors on pointers.
    *   Forgetting the array must be sorted.
    *   Integer overflow when calculating `mid` (mitigated by using `left + (right - left) // 2`).

---

## **4. ✅ Solved Problems Log**
*(For each problem you solve, add a quick entry. Focus on the insight, not the code.)*

| Problem Name | Difficulty | Key Insight & Why This Pattern | Edge Cases | Date Solved |
| :--- | :--- | :--- | :--- | :--- |
| [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Classic template application. Array is sorted, need O(log n) time. | Single element, target not present | [Date] |
| [34. Find First and Last...](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Use two passes: one with `condition: nums[mid] >= target` (find start), one with `condition: nums[mid] > target` (find end). | Empty array, target not found | [Date] |
| [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Compare `nums[mid]` to `nums[right]` to know which side is sorted. The min is always in the unsorted side. | Already sorted array, two elements | [Date] |
| | | | | |

---

## **5. 📚 Resources & Links**
*   **AlgoMonster Concept Link:** [Binary Search](https://algo.monster/problems/binary_search_intro)
*   **NeetCode Video Explanation:** [Binary Search](https://www.youtube.com/watch?v=s4DPM8ct1pI)
