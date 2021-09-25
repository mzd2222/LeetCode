def singleNumber(nums):


    b = set(nums)

    a = sum(nums) - 2 * sum(b)

    print(b)
    print(a)


a = [2,2,1]

singleNumber(a)