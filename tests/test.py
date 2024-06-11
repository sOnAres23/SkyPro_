a = "Счет 73654108430135874305"
b = a[:-20]
print(b)

c = "Visa Platinum 8990922113665229"
d = c[:-16]
print(d)

nums = [-5, -7, -9, -13]

max_nums = []

for i in nums:
    if i < 0:
        if i == min(nums):
            max_nums.append(i)
            nums.remove(i)


