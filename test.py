def isPalindrome(s: str):
    s = s.lower()
    a = ""
    for i in s:
        if i.isalpha() or i.isdigit():
          a += i

    if len(a) <= 1:
        # print(1)
        return True

    print(a)

    if len(a) % 2 == 0:
        print(a[:int(len(a)/2)])
        print(a[:int(len(a)/2)-1:-1])
        if a[:int(len(a)/2)] == a[:int(len(a)/2)-1:-1]:
            print(2)
            return True
        else:
            print(3)
            return False
    else:
        print(a[:int(len(a)/2)], " ", a[:int(len(a)/2):-1])
        if a[:int(len(a)/2)] == a[:int(len(a)/2):-1]:
            print(4)
            return True
        else:
            print(5)
            return False

s = "0P"
print(isPalindrome(s))


