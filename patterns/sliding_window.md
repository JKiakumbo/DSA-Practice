# **Coding Pattern Notes**

**Pattern Name:** Sliding Window
**Status:** Learning
**Date Started:** 13.10.2025
**Date Mastered:** [Date]

---

## **1. 🧠 Pattern Overview**

* **Core Concept:** Sliding window problems are a variant of the same direction two pointers problems.
  The function performs on the entire interval between the two pointers instead of only at the two positions.
  Usually, we keep track of the overall result of the window, and when we "slide" the window (insert/remove an item),
  we simply manipulate the result to accommodate the changes to the window. Time complexity wise, this is much more
  efficient as we do not recalculate the overlapping intervals between two windows over and over again. We try to reduce
  a nested loop into two passes on the input (one pass with each pointer).

* **Categories:**
  * Fixed Size: The two pointers start at the same position and move in the same direction, but at different speeds.
  * Flexible Shortest: The two pointers start at the start of the array and move forward.
  * Flexible Longest: The two pointers start at the start of the array and move forward.
* **When to Use (Key Signals):**
    * Signal 1: Problems involving arrays/lists, subarrays, substrings, or a contiguous set of elements.
    * Signal 2: Key phrases like "contiguous," "subarray," "substring "largest/smallest sum," "longest/shortest length."
    * Signal 3: Problems that require finding an optimal solution (e.g., maximum, minimum, longest, shortest) within a contiguous segment of the input.
    * Signal 4: Problems that can be solved by maintaining a dynamic window of elements that expands and contracts based on certain conditions.
    * Signal 5: Problems that involve frequency counts or character counts within a substring or subarray.
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## **2. 📝 The Universal Template**

*(This is the most important section. Keep the code clean and commented.)*
### **Fixed Size**
```python
def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans

```
**Template Breakdown & Notes:**
* **Initialization:** answer and window are initialized to the first window of the given size.
* **Loop Condition:** We use `for right in range(window_size, len(input))` to ensure we check all elements starting from the end of the first window.
* **Pointer Movement:** The `right` pointer moves forward, and the `left` pointer is calculated based on the `right` pointer and the fixed window size.
* **Processing Elements:** The elements at the `left` and `right` pointers are processed together, which is often the core of the problem being solved.
* **Return Value:** The return value will depend on the specific problem being solved, often involving the `ans` variable.

### **Flexible Shortest**
```python
def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while valid(window):
            ans = min(ans, window)      # window is guaranteed to be valid here
            remove input[left] from window
            left += 1
    return ans

```

**Template Breakdown & Notes:**

* **Initialization:** answer and window are initialized. The left pointer starts at the beginning of the input.
* **Loop Condition:** We use `for right in range(len(input))` to ensure we check all elements.
* **Pointer Movement:** The `right` pointer moves forward, and the `left` pointer moves forward based on the validity of the window.
* **Processing Elements:** The elements at the `left` and `right` pointers are processed together, which is often the core of the problem being solved.
* **Condition Function:** This function determines whether the current window is valid based on the problem's requirements.
* **Return Value:** The return value will depend on the specific problem being solved, often involving the `ans` variable.

### **Flexible Longest**
```python
def sliding_window_flexible_longest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while invalid(window):        # update left until window is valid again
            remove input[left] from window
            left += 1
        ans = max(ans, window)        # window is guaranteed to be valid here
    return ans

```

**Template Breakdown & Notes:**

* **Initialization:** answer and window are initialized. The left pointer starts at the beginning of the input.
* **Loop Condition:** We use `for right in range(len(input))` to ensure we check all elements.
* **Pointer Movement:** The `right` pointer moves forward, and the `left` pointer moves forward based on the validity of the window.
* **Processing Elements:** The elements at the `left` and `right` pointers are processed together, which is often the core of the problem being solved.
* **Condition Function:** This function determines whether the current window is invalid based on the problem's requirements.
* **Return Value:** The return value will depend on the specific problem being solved, often involving the `ans` variable.

---

## **3. 🔄 Variations & Common Tricks**
* **Variation 1: Subarray with Maximum Sum (Fixed Size)**
    * `Condition:` Maintain a fixed-size window and update the sum as the window slides.
* **Variation 2: Longest Substring with At Most K Distinct Characters (Flexible Longest)**
    * `Condition:` Expand the window by moving the right pointer and contract it by moving the left pointer when the number of distinct characters exceeds K.
* **Variation 3: Minimum Size Subarray Sum (Flexible Shortest)**
    * `Condition:` Expand the window by moving the right pointer and contract it by moving the left pointer when the sum of the window is greater than or equal to the target.
* **Common Pitfalls:**
    * Forgetting to initialize the window correctly.
    * Not handling edge cases, such as empty arrays or single-element arrays.
    * Off-by-one errors when calculating the left pointer in fixed-size windows.
---

## **4. ✅ Solved Problems Log**

*(For each problem you solve, add a quick entry. Focus on the insight, not the code.)*

| Problem Name                                                                                          | Difficulty | Key Insight & Why This Pattern                                     | Edge Cases                         | Date Solved |
|:------------------------------------------------------------------------------------------------------|:-----------|:-------------------------------------------------------------------|:-----------------------------------|:------------|
| [Find the First True in a Sorted Boolean Array](https://algo.monster/problems/binary_search_boundary) | Easy       | Classic template application. Array is sorted, need O(log n) time. | Single element, target not present | 23-09-2025  |

---

## **5. 📚 Resources & Links**
* **AlgoMonster Concept Link:** [Sliding Window](https://algo.monster/problems/subarray_sum_fixed)
