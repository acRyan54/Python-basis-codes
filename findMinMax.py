def find(l):
    if l == []:
        return (None, None)
    min = max = l[0]
    for x in l:
        if min > x:
            min = x
        if max < x:
            max = x
    return(min, max)

l = list( map(int, input().split()))
print(find(l))