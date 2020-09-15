#5
def Per(n):
    i = 0
    ch = []
    while i <= n:  
        b = 1
        while b <= i:
            ch.append(str(i))
            b += 1
            if len(ch) == n:
                return ch
        i += 1
print(' '.join(Per(10)))