def trim(s):
    head = 0; tail = -1
    while s[head] == ' ':
        head += 1
    while s[tail] == ' ':
        tail -= 1
    if tail == -1:
        return s[head: ]
    else:
        return s[head: tail + 1]
