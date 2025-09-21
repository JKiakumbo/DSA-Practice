# **Learning Process**

**Goal:** Deeply understand the pattern and its variations, not to solve quickly.
**Mindset:** Embrace struggle, but don't spin your wheels endlessly. The 20-minute rule is your friend.

## **Step 0: Preparation (Before You Start)**
*   **Have Open:** Your AlgoMonster concept page for the pattern you're learning (e.g., the "Binary Search" article).
*   **Have Ready:** Your digital note template for that pattern, specifically the "Universal Template" section.

## **Step 1: Cursory Problem Read & Pattern Identification (1-2 mins)**
*   Read the problem. Don't deep-dive yet.
*   Ask yourself: **"Does this problem have the key signals for my current pattern?"** (e.g., "Is the array sorted? Yes. This is likely a Binary Search problem.").
*   The answer should almost always be "yes" because you're doing focused practice. This step is to build the reflex of checking for key signals.

## **Step 2: Deep Comprehension & Examples (5 mins)**
*   Now, read the problem carefully. Underline key constraints.
*   **Define your function signature:** What are the inputs and the output?
*   **Create 2-3 examples,** including a small edge case. Write them down on paper or in your notebook.
    *   Example 1: Normal case
    *   Example 2: Edge case (empty input, not found, etc.)

## **Step 3: Template Recall & Adaptation (The Core Step) (5-10 mins)**
*   **Do NOT start coding from scratch.**
*   Look at your notes and **copy the universal template** for the pattern into your code editor. (e.g., the generic Binary Search loop with `left`, `right`, and `mid`).
*   **Now, adapt it.** This is the crucial learning moment. Ask yourself:
    *   What does the `condition(mid)` function need to be for *this specific problem*?
    *   Do I need to adjust the loop condition (`while left <= right` vs. `<`)?
    *   What should I return at the end (`left`, `right`, or something else`)?
*   **Pseudocode the adaptation first.** Write comments inside the template outlining your logic.

## **Step 4: Implement & Test (10-15 mins)**
*   **Implement your adapted template.** Write the code.
*   **Immediately test it with your examples from Step 2.**
*   **DO NOT RUN THE CODE YET.** Do a **dry run on paper**. Step through your code line by line with your example input. Track every variable. This is the single best way to build debugging skills and truly understand how your code works.
*   Only after your dry run checks out, run the code for real.

## **Step 5: Debug and Learn (As long as it takes)**
*   **If it fails:** This is expected and where the deepest learning happens!
*   **Don't panic.** Check the failing test case.
*   **Go back to your dry run.** Where did your mental model differ from the actual code? The bug is almost always in your adaptation of the template's condition or pointer update logic.
*   **The 20-Minute Rule:** If you're truly stuck for 20 minutes, **stop coding.**
    *   **Re-read the AlgoMonster concept section** for the pattern.
    *   Look at the solution **only to understand the specific adaptation** you missed. (e.g., "Ah, for finding the first occurrence, I need to use `>=` in the condition and return `left`").
    *   **Do not just copy the solution.** Understand the *why*, then close the solution and implement it yourself.

## **Step 6: Note-Taking & Assimilation (5 mins)**
*   **This is non-negotiable.** After you solve the problem (whether by yourself or with help), go to your digital notes for that pattern.
*   **Add the problem** to your "Solved Problems Log" table.
*   **Write the "Key Insight".** This is the most important part. What was the trick to adapting the template? Example:
    *   *"Key Insight: For 'Find First Bad Version', the `is_valid(mid)` function is `isBadVersion(mid)`. When it returns True, I found a bad version, but I need to search left to see if an earlier one exists, so I set `right = mid - 1`."*
*   **Note any edge cases** that caused trouble.

---

By using this more deliberate process during your learning weeks, you will build a much stronger foundation. When you later start the AlgoMonster 50 list, you'll be surprised at how quickly and confidently you can solve problems because you took the time to learn the *why* behind the *how*.