import random
nums = [random.randint(-1000, 1000) for i in range(1000)]

min_i = nums.index(min(nums))
max_i = nums.index(max(nums))
n = 0
if min_i > max_i:
    min_i, max_i = max_i, min_i
for i in range (min_i, max_i+1):
    if nums[i] < 0:
        n += 1
print(n)
    
