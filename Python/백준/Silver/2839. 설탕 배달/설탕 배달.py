N = int(input())

# 자료 구조 정의
# 5kg와 3kg의 최대 봉지수 
max_5 = N // 5 
max_3 = N // 3
min_bag = max_5 + max_3
isFind = False
# 알고리즘

for num_5 in range(max_5+1):
    for num_3 in range(max_3+1):
        if num_5*5 + num_3*3 == N:
            isFind = True
            current_bag = num_5 + num_3
            if min_bag > current_bag:
                min_bag = current_bag


if isFind : # N kg이 되는 봉지수가 없으면 
    print(min_bag)
else:
    print(-1)