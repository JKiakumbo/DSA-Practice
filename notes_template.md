# **Pattern Name: [e.g., Binary Search]**
**Status:** [Not Started / Learning / Practicing / Mastered]
**Date Started:** [Date]
**Date Mastered:** [Date]

---

## **1. 🧠 Pattern Overview**
*   **Core Concept:** [1-2 sentence description in your own words. E.g., "Divide and conquer method for searching in a sorted array by repeatedly halving the search interval."]
*   **When to Use (Key Signals):**
    *   [Signal 1: e.g., "The input array is sorted"]
    *   [Signal 2: e.g., "Problem requires O(log n) time complexity"]
    *   [Signal 3: e.g., "Finding a specific value, first/last position, or min/max value"]
*   **Time Complexity:** [e.g., O(log n)]
*   **Space Complexity:** [e.g., O(1) for iterative implementation]

---

## **2. 📝 The Universal Template**
*(This is the most important section. Keep the code clean and commented.)*

```python
def template_function(array, target) -> int:
    # Initialize pointers
    left, right = 0, len(array) - 1

    # Core loop condition
    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow

        # The central condition check
        if condition(mid, target, array):
            right = mid - 1   # Search left half
        else:
            left = mid + 1    # Search right half

    # Post-processing: what to return?
    return left

def condition(mid, target, array) -> bool:
    # Define the condition that makes 'mid' valid.
    # Example: return array[mid] >= target  (for finding first occurrence)
    return
```
**Template Breakdown & Notes:**
*   **Loop Condition:** `while left <= right` vs `while left < right` is used for...
*   **Mid Calculation:** `left + (right - left) // 2` is safer than `(left+right)//2` because...
*   **The Condition Function:** This is the key to adapting the template. It defines what we are searching for.
*   **Return Value:** Often we return `left`, but sometimes it's `right` or `array[left]`. It depends on the condition.

---

## **3. 🔄 Variations & Common Tricks**
*   **Variation 1: Finding an Exact Match**
    *   Code Snippet:
        ```python
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        ```
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
*   **AlgoMonster Concept Link:** [Insert Link Here]
*   **Helpful LeetCode Discuss Post:** [Insert Link Here]
*   **NeetCode Video Explanation:** [Insert Link Here]
