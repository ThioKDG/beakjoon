import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    temp = input().split()
    
    info.append([int(temp[0]), temp[1]])

info.sort(key=lambda x: x[0])

for user in info:
    print(user[0], user[1])