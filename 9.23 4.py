from typing import List

def detectSameNumber(nums: List, hash_num: int):

    hash = []

    for i in range(hash_num):
        hash.append([])

    for i in nums:

        num_hash = i % hash_num

        if i in hash[num_hash]:
            return True

        else:
            hash[num_hash].append(i)

    return False


a = [1,2,3,4,5,6,7,9]

print(detectSameNumber(a, 3))
