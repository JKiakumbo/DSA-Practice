# Middle of a Linked List

## Problem Metadata
- **Name:** Remove Duplicates
- **Link:** https://algo.monster/problems/middle_of_linked_list
- **Difficulty:** Easy
- **Pattern:** Two Pointers
- **Tags:** two-pointers, linked-list, fast-and-slow-pointer

## Key Dates
- **First Attempt:** 07-10-2025
- **Solved On:** 07-10-2025
- **Time Spent:** 10 minutes

## Solution
```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.val
```

## Approach Steps
1. Initialize two pointers, `slow` and `fast`, both starting at the head of the linked list.
2. Iterate through the linked list with the `fast` pointer moving two steps at a time and the `slow` pointer moving one step at a time.
3. Continue this until the `fast` pointer reaches the end of the list (i.e., `fast` is `None` or `fast.next` is `None`).
4. At this point, the `slow` pointer will be at the middle node of the linked list.
5. Return the value of the `slow` pointer.

## Complexity
- **Time:** O(n)
- **Space:** O(1)

## Lessons Learned
### Key Insights
- Using two pointers allows for efficient traversal of the linked list.
- The `slow` pointer tracks the middle of the list while the `fast` pointer moves quickly to the end.
- Handling edge cases such as empty lists or lists with a single node.
- Understanding that when the list has an even number of nodes, the `slow` pointer will point to the second middle node.

### What Worked Well
- Clear logic for moving pointers.
- Efficient traversal of the linked list.

### Challenges Faced
- Remembering to check both `fast` and `fast.next` in the while loop condition.

### For Next Time
- Practice more problems involving linked list manipulation to solidify understanding.
- Focus on edge cases in linked list problems.
- Review the two-pointer technique in different contexts.
