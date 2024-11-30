# 나는 공포도가 높은 사람 기준으로 뒤에서 끊어내는 방식  
# -> 그룹 크기가 커지고 최대 개수를 뽑아낼 수 없음

# 그러므로, 앞에서부터 모험자 수가 현재 공포도 이상이라면 그룹 결성 및 카운트

n = int(input()) 
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력


# # 잘못된 코드
# n = int(input())
# array = list(map(int,input().split()))
# count = 0

# def func(array):
#     count = 0
#     array.sort()
#     while array and len(array) >= array[-1]:
#         max_val = array[-1]
#         array = array[:-max_val]
#         count += 1
#     return count

# print(func(array))