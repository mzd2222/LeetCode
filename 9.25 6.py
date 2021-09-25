from typing import List


def intersect(nums1: List[int], nums2: List[int]):

    a = []

    for i in nums1:
        if i in nums2:
            a.append(i)
            nums2.remove(i)

    return a


print(intersect([1,1,2,2,3], [2,3,3,1,1]))