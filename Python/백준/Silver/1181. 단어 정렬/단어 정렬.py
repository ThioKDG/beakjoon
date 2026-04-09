N = int(input())

li = []
for i in range(N):
    li.append(input())

setli = set(li)
li = list(setli)

li.sort()
li.sort(key = len)
for i in li:
    print(i)