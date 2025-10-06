# **Coding Pattern Notes**

**Pattern Name:** Two Pointers
**Status:** Learning
**Date Started:** 06.10.2025
**Date Mastered:** [Date]

---

## **1. 🧠 Pattern Overview**

* **Core Concept:** Two pointers is a common interview technique often used to solve certain problems involving an iterable data structure, such as an array.
As the name suggests, this technique uses two (or more) pointers that traverse through the structure.
The pointers can move at different speeds or directions depending on the problem requirements. 
This technique is particularly useful for problems involving searching, sorting, or partitioning data.
Two pointer algorithm has these characteristics:
  * Two moving pointers, regardless of directions, moving dependently or independently;
  * A function that utilizes the entries referenced by the two pointers, which relates to the answer in a way;
  * An easy way of deciding which pointer to move;
  * A way to process the array when the pointers are moved.
* **Categories:**
  * Same Direction: The two pointers start at the same position and move in the same direction, but at different speeds.
  * Opposite Direction: The two pointers start at the two ends of the array and move towards each other.
* **When to Use (Key Signals):**
    * Signal 1: Problems involving arrays or linked lists where you need to find pairs or triplets that satisfy a certain condition.
    * Signal 2: Problems that require partitioning or rearranging elements based on a condition.
    * Signal 3: Problems that involve searching for a specific value or combination of values in a sorted array.
* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## **2. 📝 The Universal Template**

*(This is the most important section. Keep the code clean and commented.)*
### **Same Direction**
```python
def two_pointers_same(arr):
    slow, fast = 0, 0
    while fast < len(arr):
        # Process current elements
        current = process(arr[slow], arr[fast])

        # Update pointers based on condition
        if condition(arr[slow], arr[fast]):
            slow += 1

        # Fast pointer always moves forward
        fast += 1
```
**Template Breakdown & Notes:**
* **Initialization:** Two pointers are initialized at the start of the array (or both at the start for same direction).
* **Loop Condition:** We use `while fast < len(arr)` to ensure we check all elements.
* **Pointer Movement:** The `fast` pointer always moves forward, while the `slow` pointer moves based on a condition.
* **Processing Elements:** The elements at the `slow` and `fast` pointers are processed together, which is often the core of the problem being solved.
* **Condition Function:** This function determines when to move the `slow` pointer, based on the relationship between the elements at the two pointers.
* **Return Value:** The return value will depend on the specific problem being solved, often involving the `slow` pointer.

### **Opposite Direction**
```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process current elements
        current = process(arr[left], arr[right])
        
        # Update pointers based on condition
        if condition(arr[left], arr[right]):
            left += 1
        else:
            right -= 1
```

**Template Breakdown & Notes:**

* **Initialization:** Two pointers are initialized at the start and end of the array (or both at the start for same direction).
* **Loop Condition:** We use `while left < right` to ensure the pointers do not cross each other.
* **Pointer Movement:** The `left` pointer moves forward and the `right` pointer moves backward based on a condition.
* **Processing Elements:** The elements at the `left` and `right` pointers are processed together, which is often the core of the problem being solved.
* **Condition Function:** This function determines which pointer to move, based on the relationship between the elements at the two pointers.
* **Return Value:** The return value will depend on the specific problem being solved, often involving the `left` or `right` pointer.

---

## **3. 🔄 Variations & Common Tricks**
* **Variation 1: Finding Pairs with a Given Sum**
    * `Condition:` If the sum of elements at `left` and `right` equals the target, move both pointers. If the sum is less than the target, move the `left` pointer. If the sum is greater than the target, move the `right` pointer.
* **Variation 2: Removing Duplicates from a Sorted Array**
*   * `Condition:` If the current element is not equal to the last unique element, move the `slow` pointer and update the last unique element.
* **Variation 3: Partitioning an Array**
    * `Condition:` If the current element is less than a pivot value, swap it with the element at the `slow` pointer and move both pointers. If it's greater or equal, just move the `fast` pointer.
* **Common Pitfalls:**
    * Off-by-one errors on pointers.
    * Forgetting to handle edge cases, such as empty arrays or single-element arrays.
---

## **4. ✅ Solved Problems Log**

*(For each problem you solve, add a quick entry. Focus on the insight, not the code.)*

| Problem Name                                                                                          | Difficulty | Key Insight & Why This Pattern                                     | Edge Cases                         | Date Solved  |
|:------------------------------------------------------------------------------------------------------|:-----------|:-------------------------------------------------------------------|:-----------------------------------|:-------------|
| [Find the First True in a Sorted Boolean Array](https://algo.monster/problems/binary_search_boundary) | Easy       | Classic template application. Array is sorted, need O(log n) time. | Single element, target not present | [23-09-2025] |

---

## **5. 📚 Resources & Links**
* **AlgoMonster Concept Link:** [Two Pointers](https://algo.monster/problems/two_pointers_intro)
* **NeetCode Video Explanation:** [Binary Search](https://www.youtube.com/watch?v=xZ4AfXHQ1VQ&t=3s)
