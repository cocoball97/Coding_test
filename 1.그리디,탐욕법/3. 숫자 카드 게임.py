n, m = map(int, input().split())

lst = []
max = 0

for i in range(n):
    data =list(map(int, input().split()))
    if max<min(data):
        max = min(data)

print(max)
    