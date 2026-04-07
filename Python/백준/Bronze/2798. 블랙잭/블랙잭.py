N, M = map(int, input().split())

card_list = list(map(int, input().split()))


def findMax():
    max = 0
    for card1_index in range(N-2):
        for card2_index in range(card1_index+1, N-1):
            for card3_index in range(card2_index+1, N):
                sum = card_list[card1_index] + card_list[card2_index] + card_list[card3_index] 
                if sum == M: return sum # M과 같아지면 그만하기
                elif max < sum < M : # max =0 이니까 목표값보다는 작지만 순환하면서 설정된 최대값보다 크면 최대값 업데이트
                    max = sum
    return max
                
print(findMax())


 