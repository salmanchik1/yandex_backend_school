a, b = input(), input()
s, p, u = set(), set(), set()
n = len(b)
for j in range(n):
    if b[j] == a[j]:
        p.add(j)
for j in range(n):
    if j not in p:
        for i in range(n):
            if i not in u and i not in p and a[i] == b[j]:
                s.add(j)
                u.add(i)
                break
r = ('P' if i in p else 'S' if i in s else 'I' for i in range(n))
print(''.join(r))
