def product_of_array_except_self(nums: list[int]) -> list[int]:
    size = len(nums)
    ans = [1] * size

    left = 1
    for i in range(size):
        ans[i] = left
        left *= nums[i]

    right = 1
    for i in reversed(range(size)):
        ans[i] *= right
        right *= nums[i]

    return ans