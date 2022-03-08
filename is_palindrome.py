def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

n = int(input())
print(list(filter(isPalindrome, range(1, n+1))))