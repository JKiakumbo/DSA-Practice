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