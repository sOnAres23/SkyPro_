def numbers(nums: list) -> int:
    max_nums = []
    if len(nums) < 2:
        return 0
    if all(x > 0 for x in nums):
        for i in nums:
            if i == max(nums):
                max_nums.append(i)
                nums.remove(i)
        for i in nums:
            if i == max(nums):
                max_nums.append(i)
                nums.remove(i)
    else:
        for i in nums:
            if i == min(nums):
                max_nums.append(i)
                nums.remove(i)
        for i in nums:
            if i == min(nums):
                max_nums.append(i)
                nums.remove(i)
    return max_nums[0] * max_nums[1]


print(numbers([2, 3, 5, 7, 11]))
print(numbers([-5, -10, -9, -12]))
print(numbers([2, 4]))
print(numbers([23]))
