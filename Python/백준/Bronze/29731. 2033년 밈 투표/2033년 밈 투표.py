import sys
input = sys.stdin.readline

N = int(input())

S = ['Never gonna give you up', 
     'Never gonna let you down', 
     'Never gonna run around and desert you',
     'Never gonna make you cry',
     'Never gonna say goodbye',
     'Never gonna tell a lie and hurt you',
     'Never gonna stop'
    ]

for i in range(N):
    inString = input().strip()
    if inString not in S:
        print('Yes')
        break
else:
    print('No')