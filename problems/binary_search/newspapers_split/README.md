# Newspapers

## Problem Metadata
- **Name:** Find the First True in a Sorted Boolean Array
- **Link:** https://algo.monster/problems/newspapers_split
- **Difficulty:** Hard
- **Pattern:** Binary Search
- **Tags:** array, binary-search, boundary-search, newspapers-split

## Key Dates
- **First Attempt:** 01-10-2025
- **Solved On:** 01-10-2025
- **Time Spent:** 60 minutes

## Solution
```python
from typing import List

def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    left, right = max(newspapers_read_times), sum(newspapers_read_times)
    boundary_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if get_number_of_needed_workers(newspapers_read_times, mid) <= num_coworkers:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

def get_number_of_needed_workers(read_times: List[int], limit: int) -> int:
    workers = 1
    time = 0

    for read_time in read_times:
        if time + read_time > limit:
            workers += 1
            time = read_time
        else:
            time += read_time

    return workers
```

## Approach Steps
1. Initialize left and right pointers with the maximum single newspaper read time and the total read time respectively, and a variable to store boundary index
2. While left <= right, calculate mid
3. Use a helper function to determine the number of coworkers needed if each coworker can read up to mid time
4. If the number of needed coworkers is less than or equal to available coworkers, update boundary index and move right pointer
5. If the number of needed coworkers is greater than available coworkers, move left pointer
6. Return boundary index after loop
7. Define a helper function to calculate the number of coworkers needed given a time limit
8. Iterate through the read times, accumulating time until it exceeds the limit, then increment the coworker count and reset the accumulated time
9. Return the total number of coworkers needed

## Complexity
- **Time:** O(log(n))
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Binary search can efficiently find the optimal minimum read time by narrowing down the range
- Need to handle case where a single newspaper's read time exceeds the mid value
- The helper function is crucial for determining feasibility of the current mid value
- Understanding the relationship between read times and number of coworkers is key to solving the problem


### What Worked Well
- With a little bit of hint, I was able to initialize the left and right pointers correctly
- With hint, I was able to define the feasible condition correctly

### Challenges Faced
- I struggled initially to define the feasible condition correctly
- Understanding how to partition the newspapers among coworkers based on read times

### For Next Time
- Practice more binary search variations
- Study partitioning problems in more depth
- Explore other boundary search problems