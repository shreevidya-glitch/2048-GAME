```python
import random

b = [[0]*4 for i in range(4)]

def show():
    for r in b:
        print(*[x or "." for x in r])

def add():
    e = [(i,j) for i in range(4) for j in range(4) if not b[i][j]]
    if e:
        i,j = random.choice(e)
        b[i][j] = random.choice([2,4])

def left():
    for i in range(4):
        r = [x for x in b[i] if x]
        for j in range(len(r)-1):
            if r[j] == r[j+1]:
                r[j:j+2] = [r[j]*2]
        b[i] = r + [0]*(4-len(r))

add()
add()

while True:
    print("\n--- 2048 ---")
    show()

    k = input("Move (a/d/w/s, q=quit): ").lower()

    if k == "q":
        break

    if k == "a":
        left()

    elif k == "d":
        b[:] = [r[::-1] for r in b]
        left()
        b[:] = [r[::-1] for r in b]

    elif k in "ws":
        b[:] = [list(x) for x in zip(*b)]

        if k == "s":
            b[:] = [r[::-1] for r in b]

        left()

        if k == "s":
            b[:] = [r[::-1] for r in b]

        b[:] = [list(x) for x in zip(*b)]

    add()
```
