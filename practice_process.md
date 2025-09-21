# **Practice Process**

Aim to spend **30-45 minutes** total on this process for a medium problem. Set a timer to simulate interview conditions.

---

## **Phase 1: Comprehension & Strategy (5-10 Minutes)**

**Goal:** Truly understand the problem and devise a plan before writing a single line of code.

1.  **Read the Problem Carefully:** Read it twice. Out loud if possible.
2.  **Clarify Ambiguity (Ask Questions):** Immediately ask clarifying questions as you would in an interview. If you're practicing alone, write down your assumptions.
    *   *"What are the input types and sizes?"*
    *   *"What if the input is empty?"*
    *   *"Can there be negative numbers? Duplicates?"*
    *   *"Should I modify the input data structure or return a new one?"*
3.  **Identify Input/Output:** Write down 2-3 concrete examples, including edge cases.
    *   **Example 1:** Normal case
    *   **Example 2:** Edge case (empty input, single element, extremely large value)
    *   **Example 3:** Another edge case (duplicates, negative numbers)
4.  **Brainstorm & Pattern Recognition (The "P" in PTS):** This is the crucial step. Look at the problem and your examples. Mentally scan your **Pattern Cheat Sheet**.
    *   **Is the array sorted?** -> **Binary Search**.
    *   **Do I need to find subsets/combinations/permutations?** -> **Backtracking**.
    *   **Is it about trees/graphs and levels or shortest path?** -> **BFS**.
    *   **Does it involve overlapping subproblems?** -> **Dynamic Programming**.
    *   **Do I need the top/least K elements?** -> **Heap**.
5.  **Verbally Justify Your Choice:** Say it out loud: *"I think this is a Binary Search problem because the array is sorted, and we need to find a value in O(log n) time."* This cements your reasoning.
6.  **Outline the Approach:** In plain English or pseudocode, write down the steps.
    *   *"Step 1: Initialize left and right pointers."*
    *   *"Step 2: While left <= right, calculate mid."*
    *   *"Step 3: If nums[mid] == target, return mid."*
    *   *"Step 4: Else if target is greater, search right. Else, search left."*
    *   *"Step 5: If not found, return -1."*

---

## **Phase 2: Implementation (10-20 Minutes)**

**Goal:** Translate your plan into clean, bug-free code using your templates.

1.  **Recall the Template (The "T" in PTS):** Recall the universal template for your chosen pattern from memory. Write it down as a starting point in your code editor.
2.  **Adapt the Template to the Problem:** Now, modify the generic template to fit the specific problem.
    *   Rename variables if needed (`start` and `end` instead of `left` and `right`).
    *   **Define the Core Condition:** This is the most important adaptation. What goes inside the `if` statement? (e.g., `if nums[mid] >= target:` for finding the first position).
3.  **Code with Confidence:** Write the code. Don't try to get fancy. Your goal is to correctly apply the known pattern.

---

## **Phase 3: Testing & Debugging (5-10 Minutes)**

**Goal:** Verify your code works before declaring victory. **NEVER SKIP THIS STEP.**

1.  **Dry Run with Your Example:** Take the small, concrete example you wrote down in Phase 1. **Execute your code line-by-line on paper or your notebook.**
    *   Track the value of every single variable (`left`, `right`, `mid`, `result`, etc.) at each step.
    *   This will expose almost all "off-by-one" errors and logic flaws.
2.  **Test with Edge Cases:** Now, run your code through the edge cases you identified (empty input, single element, etc.). Does it handle them correctly?
3.  **Fix Bugs:** If you find a discrepancy between your dry run and expected output, trace back to find the exact line where the logic went wrong. Fix it.

---

## **Phase 4: Review & Reflect (5 Minutes Post-Solve)**

**Goal:** Solidify the learning and improve for next time. This is how you turn one solved problem into ten lessons.

1.  **Analyze the Solution:** Once your code passes, compare it to the official solution or highly-rated answers. **Don't look for major differences; look for elegance.**
    *   Was there a more efficient way?
    *   Could the code be cleaner?
2.  **Update Your Notes (The "S" for Speedrun Knowledge):** This is the final, crucial step. In your digital notes for this pattern:
    *   **Add the problem** to your "Solved Problems Log".
    *   **Write the "Key Insight"** – the one-sentence "aha!" moment that connects the problem to the pattern.
    *   **Note any tricky edge cases** you encountered.
3.  **Rate Your Performance:** Be honest with yourself.
    *   *"Did I identify the pattern immediately?"*
    *   *"Where did I get stuck? Was it the condition in the template?"*
    *   *"How was my time management?"*

This process turns problem-solving from a stressful guessing game into a predictable, repeatable ritual. The goal is not to be a genius who instantly knows the answer, but to be a **reliable engineer who can always find a solution.**