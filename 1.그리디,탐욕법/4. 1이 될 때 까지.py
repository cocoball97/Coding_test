n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n -target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    # K로 나누기
    result += 1
    n //= k 

result += (n-1)
print(result)


# 개인풀이
result = 0
# N이 K 이상이라면 계속 나누기
while n >= k:
    if n%k == 0:
        # 결과값 int 반환
        n //= k
        result += 1
        if n == 1:
            break
    else:
        n-1
        result +=1
        if n == 1:
            break

print(result)