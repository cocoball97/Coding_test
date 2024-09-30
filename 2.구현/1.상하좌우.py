n = int(input())
x, y = 1, 1
plans = input().split()

# 이동 방향과 좌표 변화 매핑
move_dict = {
    'L': (0, -1),   # 왼쪽으로 이동
    'R': (0, 1),    # 오른쪽으로 이동
    'U': (-1, 0),   # 위로 이동
    'D': (1, 0)     # 아래로 이동
}

# 입력된 이동 계획 실행
for plan in plans:
    if plan in move_dict:
        # 딕셔너리 값 가져오기
        dx, dy = move_dict[plan]
        
        # 이동 후 좌표 계산
        nx = x + dx
        ny = y + dy

        # 공간을 벗어나지 않는 경우에만 이동
        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny

# 최종 위치 출력
print(x, y)


# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # 좌표 이동 방법 외우기
# # 좌표 이동 시, x y 좌표가 반대로 이동 (x변화 -> 위아래 변화)
# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]  
# dy = [-1, 1, 0, 0]  
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]

#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue

#     # 이동 수행
#     x, y = nx, ny

# print(x, y)