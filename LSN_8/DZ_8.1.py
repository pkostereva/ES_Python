import random
nums = [random.randint(-20, 20) for i in range(20)]
a = sum(nums[0:5])
max_sum = a
i=1
print(nums)
for i in range(len(nums)):
    a = sum(nums[i:i+5])
    print(i)
    if a > max_sum:
        max_sum = a
        max_i = nums[i:i+5]
print('Максимальная сумма: ', max_sum)
print('Максимальный срез: ', max_i)
