def find_all_anagrams(original: str, check: str) -> list[int]:
    # check_size is size of the window
    original_size, check_size = len(original), len(check)
    if original_size < check_size:
        return []

    res = []
    # stores the frequency of each character in the check string
    check_counter = [0] * 26
    # stores the frequency of each character in the current window
    window = [0] * 26
    a = ord("a")  # ascii value of 'a'
    # first window
    for i in range(check_size):
        check_counter[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1
    if window == check_counter:
        res.append(0)

    for i in range(check_size, original_size):
        window[ord(original[i - check_size]) - a] -= 1
        window[ord(original[i]) - a] += 1
        if window == check_counter:
            res.append(i - check_size + 1)
    return res