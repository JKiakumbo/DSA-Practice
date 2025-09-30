# **Coding Pattern Notes**

**Pattern Name:** Binary Search
**Status:** Learning
**Date Started:** 22.09.2025
**Date Mastered:** [Date]

---

## **1. 🧠 Pattern Overview**

* **Core Concept:** Binary Search is an efficient array searching algorithm.
  It works by repeatedly dividing the search interval(limited by left and right pointers) in half to find the target
  quicker.
  The idea is to find the middle element and compare it with the target value.
  If they are not equal, the half in which the target cannot lie is eliminated,
  and the search continues on the remaining half until the target is found or the interval is empty.
* The precondition for binary search is to find a monotonic function f(x) that returns either True or False.
* **When to Use (Key Signals):**
    * Signal 1: The input array is sorted, or we make a binary decision to reduce the search range.
    * Signal 2: Problem requires O(log n) time complexity
* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

---

## **2. 📝 The Universal Template**

*(This is the most important section. Keep the code clean and commented.)*

```python
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1  # First true index
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

* **Initialization:** `left` and `right` pointers are initialized to the start and end of the array. `boundary_index` is
  initialized to -1 to indicate that we haven't found the target yet.
* **Loop Condition:** We use `while left <= right` to ensure we check all elements, including when left is equals right.
* **Mid Calculation:** `left + (right - left) // 2` is safer than `(left+right)//2` because it prevents potential
  overflow in languages with fixed integer sizes.
* **The Condition Function:** This is the key to adapting the template. It defines what we are searching for. In this
  case, `feasible(mid)` checks if the mid element meets the criteria (e.g., `arr[mid] >= target` for finding the first
  occurrence of target).
* **Return Value:** We return `boundary_index`, which is the index of the first occurrence of the target if found,
  otherwise -1.
* **Edge Cases:** Consider cases like empty arrays, single-element arrays, and when the target is not present.
* **Adaptability:** This template can be adapted for various binary search problems by changing the `feasible`
  condition.

*  **

---

## **3. 🔄 Variations & Common Tricks**

* **Variation 1: Finding an Exact Match**
    * `Condition:` `array[mid] == target` -> then return `mid`.
* **Variation 2: Finding the First Occurrence**
    * `Condition:` `array[mid] >= target` -> then return `left`.
* **Variation 3: Search in a Rotated Sorted Array**
    * Insight: One half of the array will always be sorted. Check which half and adjust pointers accordingly.
* **Common Pitfalls:**
    * Off-by-one errors on pointers.
    * Forgetting the array must be sorted.
    * Integer overflow when calculating `mid` (mitigated by using `left + (right - left) // 2`).

---

## **4. ✅ Solved Problems Log**

*(For each problem you solve, add a quick entry. Focus on the insight, not the code.)*

| Problem Name                                                                                                               | Difficulty | Key Insight & Why This Pattern                                                                                  | Edge Cases                                                                              | Date Solved  |
|:---------------------------------------------------------------------------------------------------------------------------|:-----------|:----------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|:-------------|
| [Find the First True in a Sorted Boolean Array](https://algo.monster/problems/binary_search_boundary)                      | Easy       | Classic template application. Array is sorted, need O(log n) time.                                              | Single element, target not present                                                      | [23-09-2025] |
| [First Element Not Smaller Than Target](https://algo.monster/problems/binary_search_first_element_not_smaller_than_target) | Easy       | Adapted feasible function `condition: arr[mid] >= target`.                                                      | all elements are greater or iqual target, only last elements is greater or iqual target | [24-09-2025] |
| [Find Element in Sorted Array with Duplicates](https://algo.monster/problems/binary_search_duplicates)                     | Medium     | Adapted feasible function `condition: arr[mid] >= target`. Update boundary index only when `arr[mid] == target` | all elements are greater or iqual target, only last elements is greater or iqual target | [25-09-2025] |
| [Square Root Estimation](https://algo.monster/problems/sqrt)                                                               | Medium     | Adapted feasible function `condition: mid >= n`, initialise `left = 1` and `right = n`                          | `n=0`, non-perfect square root                                                          | [26-09-2025] |
| [Find Minimum in Rotated Sorted Array](https://algo.monster/problems/min_in_rotated_sorted_array)                          | Medium     | Adapted feasible function `condition: mid <= arr[-1]`                                                           | min is last or first element, all elements are equals                                   | [30-09-2025] |

---

## **5. 📚 Resources & Links**
* **AlgoMonster Concept Link:** [Binary Search](https://algo.monster/problems/binary_search_intro)
* **NeetCode Video Explanation:** [Binary Search](https://www.youtube.com/watch?v=s4DPM8ct1pI)
