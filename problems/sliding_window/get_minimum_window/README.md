# Minimum Window Substring

## Problem Metadata
- **Name:** Minimum Window Substring
- **Link:** https://algo.monster/problems/minimum_window_substring
- **Difficulty:** Hard
- **Pattern:** Sliding Window
- **Tags:** sliding-window, string, substring, frequency-count, minimum-window

## Key Dates
- **First Attempt:** 03-11-2025
- **Solved On:** 04-11-2025

## Solution
```python
from collections import Counter, defaultdict

def get_minimum_window(original: str, check: str) -> str:
    original_size, check_size = len(original), len(check)
    if original_size < check_size:
        return ""

    def is_smaller(window1, window2):  # is window1 smaller than window2
        if window1[1] - window1[0] == window2[1] - window2[0]:
            for i in range(window1[1] - window1[0]):
                if original[window1[0] + i] != original[window2[0] + i]:
                    return original[window1[0] + i] < original[window2[0] + i]
            return False
        else:
            return window1[1] - window1[0] < window2[1] - window2[0]

    check_count = Counter(check)
    required = len(check_count.keys())
    window_count: defaultdict[str, int] = defaultdict(int)
    # initialize "empty" window of size (original_size+1)
    window = (-original_size - 1, 0)
    satisfied = 0
    left = 0

    for right in range(original_size):
        # keep track only characters that appear in check
        if original[right] in check_count:
            window_count[original[right]] += 1
            if window_count[original[right]] == check_count[original[right]]:
                satisfied += 1
        while satisfied == required:  # valid window
            if is_smaller((left, right + 1), window):  # new window is smaller than window
                window = (left, right + 1)
            if original[left] in check_count:  # delete only characters from check
                window_count[original[left]] -= 1
                # removing original[left] makes window dissatisfied
                if window_count[original[left]] < check_count[original[left]]:
                    satisfied -= 1
            left += 1

    return original[window[0] : window[1]]
```

## Approach Steps
1. Calculate the lengths of the `original` and `check` strings. If `original` is shorter than `check`, return an empty string.
2. Define a helper function `is_smaller` to compare two windows based on their sizes and lexicographical order.
3. Create a `Counter` for the `check` string to keep track of character frequencies.
4. Initialize variables to track the number of unique characters required, a window count dictionary, the current minimum window, the number of satisfied characters, and the left pointer.
5. Iterate the `right` pointer from the start to the end of the `original` string:
   - If the character at `right` is in `check_count`, update its count in `window_count`. If its count matches that in `check_count`, increment `satisfied`.
   - While `satisfied` equals `required`, indicating a valid window:
     - Use `is_smaller` to check if the current window is smaller than the previously recorded minimum window. If so, update the minimum window.
     - Move the `left` pointer to shrink the window, updating counts and `satisfied` as necessary.
6. After the loop, return the substring of `original` corresponding to the minimum window found.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- The sliding window technique can be effectively used to find minimum substrings containing all required characters.
- Maintaining character counts and a satisfaction condition helps in efficiently determining valid windows.
- Comparing windows based on size and lexicographical order ensures the correct minimum substring is returned.

### What Worked Well
- Identifying the pattern of sliding window for substring problems.


### Challenges Faced
- I was not able to come up with the solution on my own and needed to look at the solution.

### For Next Time
- Focus on breaking down the problem into smaller parts, such as maintaining counts and checking validity of windows, to better understand the sliding window approach.
- Practice more problems involving minimum or maximum substrings to strengthen understanding of the sliding window technique.
