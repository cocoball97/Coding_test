# n, m, k 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력 받기
data =list(map(int, input().split()))

data.sort()
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산    int(A / B) = A //B : 몫 구하기
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두번째로 큰 수 더하기

print(result)


# # 단순 풀이
# # n, m, k 를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())

# # N개의 수를 공백으로 구분하여 입력 받기
# data =list(map(int, input().split()))

# data.sort()
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두번째로 큰 수

# result = 0

# while True:
#     for _ in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0:
#             break
#         result += first 
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1


# print(result)
    