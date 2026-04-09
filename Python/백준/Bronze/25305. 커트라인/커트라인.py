import sys
input = sys.stdin.readline

N, K = map(int, input().split())

X = list(map(int, input().split()))

X.sort(reverse=True)

count = 0

print(X[K-1])
    
