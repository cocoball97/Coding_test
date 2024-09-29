n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
	count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
	n %= coin
    
print(count)


# 나였으면 if 문으로 하나하나 조건문을 걸었을텐데, 리스트로 한번에 가능하네