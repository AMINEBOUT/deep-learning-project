def update(nums):
    nums_copy = nums
    for i in range(len(nums_copy)):
        nums_copy.append(nums[i]*2)
    return nums_copy


arr = [1, 2, 3]
print(update(arr))