N, K = map(int, input().split())

coin_list = []

for i in range(N):
    coin_list.append(int(input()))
    
coinCount = 0

for coin in coin_list[::-1]:
    if K >= coin:
        coinCount += K // coin
        K %= coin
    
print(coinCount)