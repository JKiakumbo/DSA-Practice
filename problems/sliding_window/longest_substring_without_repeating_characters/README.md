# Longest Substring without Repeating Characters

## Problem Metadata
- **Name:** Longest Substring without Repeating Characters
- **Link:** https://algo.monster/problems/longest_substring_without_repeating_characters
- **Difficulty:** Medium
- **Pattern:** Sliding Window
- **Tags:** sliding-window, string, substring, frequency-count non-repeating

## Key Dates
- **First Attempt:** 20-10-2025
- **Solved On:** 21-10-2025
- **Time Spent:** 50 minutes

## Solution
```python
from collections import defaultdict

def longest_substring_without_repeating_characters(s: str) -> int:
    ans = 0
    left = 0
    counter: dict[str, int] = defaultdict(int)

    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans
```

## Approach Steps
1. Initialize `ans` to store the length of the longest substring, `left` pointer to the start of the window, and a `counter` dictionary to keep track of character frequencies in the current window.
2. Iterate the `right` pointer from the start to the end of the string:
   - Increment the count of the character at the `right` pointer in `counter`.
   - While the count of the character at the `right` pointer exceeds 1 (indicating a repeat), shrink the window from the left by decrementing the count of the character at the `left` pointer in `counter` and incrementing `left`.
   - Update `ans` with the maximum of `ans` and the current window size (`right - left + 1`.
3. Return `ans` after the loop.


## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- To require non-repeating characters, a frequency count is essential to track occurrences.
- To remove duplicates, the left pointer must move until the duplicate is eliminated.

### What Worked Well
- Clear understanding of the sliding window concept.
- Understood the need for a frequency counter to track character occurrences.


### Challenges Faced
- Used a defaultdict to simplify frequency counting.
- Initially struggled with managing the counter while adjusting the left pointer.

### For Next Time
- Practice more problems involving sliding window techniques with character frequency tracking to solidify understanding.
- Focus on edge cases in string manipulation problems.
