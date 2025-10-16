# Find All Anagrams in a String

## Problem Metadata
- **Name:** Find All Anagrams in a String
- **Link:** https://algo.monster/problems/find_all_anagrams
- **Difficulty:** Medium
- **Pattern:** Sliding Window
- **Tags:** sliding-window, string, anagram, frequency-count

## Key Dates
- **First Attempt:** 15-10-2025
- **Solved On:** 16-10-2025
- **Time Spent:** 90 minutes

## Solution
```python
def find_all_anagrams(original: str, check: str) -> list[int]:
    # check_size is size of the window
    original_size, check_size = len(original), len(check)
    if original_size < check_size:
        return []

    res = []
    # stores the frequency of each character in the check string
    check_counter = [0] * 26
    # stores the frequency of each character in the current window
    window = [0] * 26
    a = ord("a")  # ascii value of 'a'
    # first window
    for i in range(check_size):
        check_counter[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1
    if window == check_counter:
        res.append(0)

    for i in range(check_size, original_size):
        window[ord(original[i - check_size]) - a] -= 1
        window[ord(original[i]) - a] += 1
        if window == check_counter:
            res.append(i - check_size + 1)
    return res
```

## Approach Steps
1. Calculate the lengths of the `original` and `check` strings. If `original` is shorter than `check`, return an empty list.
2. Initialize a result list `res` to store starting indices of anagrams.
3. Create two frequency count lists, `check_counter` and `window`, each of size 26 (for each letter in the alphabet).
4. Populate the frequency counts for the first window of size `check_size` in both `check_counter` and `window`.
5. Compare the two frequency counts. If they match, append `0` to `res`.
6. Slide the window across the `original` string:
   - For each new character added to the window, increment its count in `window`.
   - For the character that is removed from the window, decrement its count in `window`.
   - After updating the window, compare `window` with `check_counter`. If they match, append the starting index of the current window to `res`.
7. Return the result list `res`.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The sliding window technique is effective for problems involving contiguous subarrays or substrings.
- Maintaining a frequency count of characters allows for efficient comparison between the current window and the target anagram.
- The problem can be solved in linear time with constant space, as the frequency count arrays are of fixed size (26).
- Ensure to handle edge cases where the `original` string is shorter than the `check` string.

### What Worked Well
- Clear understanding of the sliding window concept.


### Challenges Faced
- I did not initially consider the use of frequency arrays, which made the first attempt more complex.
- I struggled with cases where the check string has repeated characters.

### For Next Time
- Practice more problems involving sliding window techniques to solidify understanding.
- Focus on edge cases in string manipulation problems.
