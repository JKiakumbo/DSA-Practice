from collections import Counter, defaultdict

def get_minimum_window(original: str, check: str) -> str:
    original_size, check_size = len(original), len(check)
    if original_size < check_size:
        return ""

    def is_smaller(window1, window2):  # is window1 smaller than window2
        if window1[1] - window1[0] == window2[1] - window2[0]:
            for i in range(window1[1] - window1[0]):
                if original[window1[0] + i] != original[window2[0] + i]:
                    return original[window1[0] + i] < original[window2[0] + i]
            return False
        else:
            return window1[1] - window1[0] < window2[1] - window2[0]

    check_count = Counter(check)
    required = len(check_count.keys())
    window_count: defaultdict[str, int] = defaultdict(int)
    # initialize "empty" window of size (original_size+1)
    window = (-original_size - 1, 0)
    satisfied = 0
    left = 0

    for right in range(original_size):
        # keep track only characters that appear in check
        if original[right] in check_count:
            window_count[original[right]] += 1
            if window_count[original[right]] == check_count[original[right]]:
                satisfied += 1
        while satisfied == required:  # valid window
            if is_smaller((left, right + 1), window):  # new window is smaller than window
                window = (left, right + 1)
            if original[left] in check_count:  # delete only characters from check
                window_count[original[left]] -= 1
                # removing original[left] makes window dissatisfied
                if window_count[original[left]] < check_count[original[left]]:
                    satisfied -= 1
            left += 1

    return original[window[0] : window[1]]