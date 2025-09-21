# Sliding Window Pattern

## When to use
- Subarray or substring problems
- Need to track a window (fixed or variable size)

## Template (Python)
```python
def sliding_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

## Example Problems
- Maximum Subarray of Size K
- Longest Substring Without Repeating Characters
