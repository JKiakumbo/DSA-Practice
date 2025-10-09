# Valid Palindrome

## Problem Metadata
- **Name:** Valid Palindrome
- **Link:** https://algo.monster/problems/valid_palindrome
- **Difficulty:** Easy
- **Pattern:** Two Pointers
- **Tags:** two-pointers, string, palindrome

## Key Dates
- **First Attempt:** 09-10-2025
- **Solved On:** 09-10-2025
- **Time Spent:** 10 minutes

## Solution
```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

## Approach Steps
1. Initialize two pointers, `left` at the start and `right` at the end of the string.
2. While `left` is less than `right`, check if the characters at these pointers are alphanumeric.
3. If the character at `left` is not alphanumeric, increment `left` and continue to the next iteration.
4. If the character at `right` is not alphanumeric, decrement `right` and continue to the next iteration.
5. If both characters are alphanumeric, compare them in a case-insensitive manner.
6. If they do not match, return `False`.
7. If they match, increment `left` and decrement `right`.
8. If the loop completes without mismatches, return `True`.


## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- The two-pointer technique is effective for checking palindromes in strings.
- Skipping non-alphanumeric characters ensures that only relevant characters are compared.
- Comparing characters in a case-insensitive manner is crucial for this problem.
- The problem can be solved in linear time without additional space.

### What Worked Well
- Clear understanding of the palindrome checking problem.
- Efficiently used two pointers to find the solution.
- Handled edge cases correctly.

### Challenges Faced
- I forgot to increment/decrement pointers after a successful match initially, which could lead to an infinite loop.

### For Next Time
- Remember to always check for edge cases, such as strings with only non-alphanumeric characters.
- Practice more two-pointer variations.
