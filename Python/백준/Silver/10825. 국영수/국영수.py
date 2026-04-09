import sys
input = sys.stdin.readline

N = int(input())

student = [input().split() for _ in range(N)]

student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])