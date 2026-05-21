nums = [2,7,11,15]
target = 9
seen = {}

print(nums)

for i,num in enumerate(nums):
    print(i,num)
    complement = target - num
    if complement in seen:
        print([seen[complement], i])