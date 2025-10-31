# Linked List Cycle

## Problem Metadata
- **Name:** Linked List Cycle
- **Link:** https://algo.monster/problems/linked_list_cycle
- **Difficulty:** easy
- **Pattern:** Fast and Slow Pointers
- **Tags:** fast-and-slow-pointer, linked-list, cycle-detection

## Key Dates
- **First Attempt:** 31-10-2025
- **Solved On:** 31-10-2025

## Solution
```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(nodes: Node) -> bool:
    if nodes == None:
        return False

    fast = nodes
    slow = nodes

    while fast != None and fast.next != None :
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

## Approach Steps
1. Check if the head node is `None`. If it is, return `False` since an empty list cannot have a cycle.
2. Initialize two pointers, `slow` and `fast`, both starting at the head of the linked list.
3. Use a `while` loop to traverse the linked list as long as `fast` and `fast.next` are not `None`.
4. Inside the loop, move the `slow` pointer one step forward and the `fast` pointer two steps forward.
5. After moving the pointers, check if `slow` is equal to `fast`. If they are equal, it indicates that there is a cycle in the linked list, so return `True`.
6. If the loop exits without the pointers meeting, return `False`, indicating that there is no cycle in the linked list.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Lessons Learned
### Key Insights
- Using two pointers (fast and slow) is an effective way to detect cycles in a linked list.
- The `fast` pointer moves at twice the speed of the `slow` pointer, so if there is a cycle, they will eventually meet.
- Handling edge cases such as an empty list or a list with a single node.
- Understanding the conditions for the `while` loop to prevent null pointer exceptions.

### What Worked Well
- Clear logic for moving pointers.
- Efficient traversal of the linked list.
- Handled edge cases correctly.
- Identified the cycle detection condition effectively.

### Challenges Faced
- No significant challenges faced during implementation.

### For Next Time
- Practice more problems involving linked list manipulation to solidify understanding.
- Focus on edge cases in linked list problems.
- Review the fast and slow pointer technique in different contexts.
