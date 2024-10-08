# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문 위치 표시 맵 생성 및 현재 캐릭터의 좌표, 방향 입력받기
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기  외우기!!!!!!!!!
array = [list(map(int, input().split())) for _ in range(n)]

# 방향 정의 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left(direction):
    return (direction - 1) % 4  # 새로운 방향 반환

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    direction = turn_left(direction)  # 방향을 업데이트
    nx, ny = x + dx[direction], y + dy[direction]

    # 회전 후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:  
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
    else:
        turn_time += 1  # 정면에 갈 수 없는 경우 회전

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx, ny = x - dx[direction], y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break  # 빠져나감
        turn_time = 0

# 정답 출력
print(count)


# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# # 변수 : d 방문 위치 표시맵 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# # 좌표에서 기초가 되는 틀 외우기
# d = [[0] * m for _ in range(n)]  


# # 현재 캐릭터의 X, Y 좌표, 방향을 입력받기
# x, y, dirextion = map(int, input().split())
# d[x][y] = 1 # 현재 좌표 방문 처리

# # 전체 맵 정보를 입력받기 
# # 리스트를 만들고 append로 추가
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))
    
# # 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 왼쪽으로 회전
# def turn_left():
#     global direction     # direction 변수가 함수 바깥에서 선언된 전역변수라서
#     direction -= 1       # 왼쪽으로 회전
#     if direction == -1:  # 북쪽에서 회전하면 서쪽 : -1 → 3
#         direction = 3

# # 시뮬레이션 시작
# count = 1    
# trun_time = 0
# while True:
#     # 왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:    # d 방문위치, array 바다위치
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1    # 한번 더 회전
#     # 네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:    # 3의 경우 : 바라보는 방향 유지, 한 칸 뒤로
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있는 경우
#         else:
#             break    # 빠져나감
#         turn_time = 0     # 다시 1의 경우로 돌아감
    
# # 정답 출력
# print(count)