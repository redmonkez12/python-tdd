def calculate_mean(nums: list[int]) -> float:
    if not nums:
        return 0

    return sum(nums) / len(nums)
