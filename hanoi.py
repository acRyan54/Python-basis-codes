N = int(input())
a, b, c = 'a', 'b', 'c'
def hanoi(n, a, b, c):
    print('    ' * (N-n) + 'hanoi(%d, %s, %s, %s)' % (n, a, b, c))
    if n == 1:
        print('    ' * (N-n+1) + 'remove(1, %s, %s)' % (a, c))
        return
    hanoi(n-1, a, c, b)
    print('    ' * (N-n+1) + 'remove(%d, %s, %s)' % (n-1, a, c))
    hanoi(n-1, b, a, c)
    
hanoi(N, a, b, c)