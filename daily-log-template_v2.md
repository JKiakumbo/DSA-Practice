# Daily Learning Log - Phase 1: Comprehension

**Date:** `[Date]`  
**Day #:** `[Day Number]`  
**Focus Pattern:** `[e.g., Sliding Window]`  
**Energy Level:** `[⚡️⚡️️⚡️ / ⚡️⚡️️ / ⚡️]` *(Pre-session)*

---

## 1. Today's Learning Objectives
*What specific aspects of this pattern do you want to understand?*

- [ ] Understand the core concept and use-cases for the pattern
- [ ] Memorize the basic algorithmic template/steps
- [ ] Identify the time and space complexity (Big O)
- [ ] Learn to identify this pattern in a problem statement

---

## 2. Resources Planned
*What will you use to learn?*

- [ ] Video: `[Link to NeetCode/AlgoExpert video]`
- [ ] Article: `[Link to GeeksforGeeks/Medium article]`
- [ ] Diagram: Draw my own visualization of the pattern

---

## 3. Key Concepts & Notes
*Explain it in your own words. This is the most important section!*

### Core Idea:
`[The Sliding Window technique is used to perform a required operation on a specific window size of a given array or linked list. It helps avoid nested loops, reducing time complexity from O(n^2) to O(n).]`

### When to Use:
`[Problems involving arrays/lists, subarrays, substrings, or a contiguous set of elements. Key phrases: "contiguous," "subarray," "substring," "largest/smallest sum," "longest/shortest length."]`

### Basic Template/Steps:
```
1. Initialize window pointers (start=0, end=0)
2. Expand the window (end++) until a condition is met
3. Once condition is met, shrink the window (start++) until it's no longer met
4. Update the answer at each valid window
```

### Big O Complexity:
- **Time:** `[O(n)]` - Each element is processed at most twice (once by `end`, once by `start`)
- **Space:** `[O(1)]` - Unless we need to store a frequency map

### Common Variations:
`[ - Fixed-length window vs. Dynamic window
  - Using a HashMap to track character frequency for substring problems
]`

---

## 4. Practice & Application
*Solidify your learning with minimal, focused practice. Do not rush.*

| Problem | Difficulty | Status | Time Spent | Key Takeaway |
|---------|------------|--------|------------|--------------|
| `[Best Time to Buy & Sell Stock]` | Easy | ✅ Solved | `[15m]` | `[This is a simple one-pass problem that uses the concept of tracking a minimum price and a max profit.]` |
| `[Longest Substring Without Repeating Characters]` | Medium | ⚠️ Struggled | `[40m]` | `[I need to use a HashMap to store the last index of each character to know where to jump the 'start' pointer.]` |
| `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

---

## 5. Review & Reflection
*Rate your understanding and plan your next steps.*

- **Self-Assessment (1-5):** `[4]` *(1 = No clue, 5 = Could teach it)*
- **What was the biggest challenge?**
  `[Remembering to update the HashMap before moving the start pointer.]`
- **What is one thing I mastered today?**
  `[I can now confidently explain the difference between a fixed and dynamic sliding window.]`
- **What do I need to review tomorrow?**
  `[I will quickly re-solve the "Longest Substring" problem from memory.]`

---

## 6. Tomorrow's Learning Preview
*What is the next pattern or the next step for this pattern?*

- [ ] Move on to the "Prefix Sum" pattern
- [ ] Practice 2 more "Medium" Sliding Window problems

---

**Total Time Spent Today:** `[1h 45m]`  
**Mood Post-Session:** `[😊 😐 😞]`