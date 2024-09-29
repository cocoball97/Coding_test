n, m = map(int, input().split())

result = 0

for i in range(n):
    data =list(map(int, input().split()))
    min_value = min(data)
    # 리스트를 비교하지 않고 최소값만을 비교
    result = max(result, min_value)
    
print(result)
    

# 비교 시, if 문 없이 min max 함수로 바로 비교 가능