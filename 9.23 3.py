from typing import List


def rotate1(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    每次移动一步 空间复杂度 O(1) 时间复杂度超了
    """

    if len(nums) > 1000:

        mask = [0 for _ in range(len(nums))]

        num_idx = 0
        num_n = nums[num_idx]

        while sum(mask) != len(nums):

            mi = (num_idx + k) % len(nums)

            if mask[mi] == 1:
                num_idx = num_idx + 1
                num_n = nums[num_idx]
            else:
                idx_next = mi

                num_record = nums[idx_next]
                nums[idx_next] = num_n
                mask[idx_next] = 1

                num_idx = idx_next
                num_n = num_record

    else:
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

    return nums


def rotate2(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    倒着移动 感觉很快
    """

    nums.reverse()
    nums.reverse()

    a = list(reversed(nums[0:k]))
    b = list(reversed(nums[k:]))

    nums[0:k] = a
    nums[k:] = b

    return a


a = [0, 1, 2, 3, 4, 5]

print(rotate1(a, 2))
