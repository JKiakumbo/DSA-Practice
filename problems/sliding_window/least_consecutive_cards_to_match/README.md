# Least Consecutive Cards to Match

## Problem Metadata
- **Name:** Least Consecutive Cards to Match
- **Link:** https://algo.monster/problems/least_consecutive_cards_to_match
- **Difficulty:** Medium
- **Pattern:** Sliding Window
  - **Tags:** sliding-window, array, frequency-count

## Key Dates
- **First Attempt:** 24-10-2025
- **Solved On:** 24-10-2025
- **Time Spent:** 30 minutes

## Solution
```python
from collections import Counter

def least_consecutive_cards_to_match(cards: list[int]) -> int:
    window: Counter[int] = Counter()
    ans = len(cards) + 1
    left = 0
    for right in range(len(cards)):
        window[cards[right]] += 1
        while window[cards[right]] == 2:
            ans = min(ans, right - left + 1)
            window[cards[left]] -= 1
            left += 1
    if ans == len(cards) + 1:
        return -1

    return ans
```

## Approach Steps
1. Import `Counter` from the `collections` module to keep track of card frequencies.
2. Initialize a `window` counter to track the frequency of cards in the current window, `ans` to store the length of the least consecutive cards to match (initialized to a value larger than the array length), and `left` pointer to the start of the window.
3. Iterate the `right` pointer from the start to the end of the `cards` array:
   - Increment the count of the card at the `right` pointer in `window`.
   - While the count of the card at the `right` pointer equals 2 (indicating a match), update `ans` with the minimum of `ans` and the current window size (`right - left + 1`), then shrink the window from the left by decrementing the count of the card at the `left` pointer in `window` and incrementing `left`.
4. After the loop, check if `ans` is still larger than the length of the array, which indicates that no match was found. If so, return `-1`.
5. Return `ans` as the length of the least consecutive cards to match.


## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- To require matching cards, a frequency count is essential to track occurrences.
- To find the least consecutive cards, the left pointer must move until a match is found.

### What Worked Well
- Clear understanding of the sliding window concept.
- Used a set to track card occurrences effectively.


### Challenges Faced
- Used a Counter to simplify frequency counting.

### For Next Time
- Practice more sliding window variations
- Review edge cases for frequency counting problems
