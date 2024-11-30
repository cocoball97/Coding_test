# 직사각형을 만드는데 필요한 4개의 점 중 3개 점표가 주어질때 나머지 하나의 좌표를 구하려고 합니다. 점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요

# 제한사항
# v는 세점의 좌표가 들어있는 2차원 배열입니다
# 좌표값은 1 이상 10억 이하 자연수입니다

lst = [list(map(int,input().split())) for _ in range(3)]
# print(lst)

# def solution(v):


#     if v[1][0]==v[0][0]:
#         x=v[2][0]
#     else:   # if v[1][0]==v[2][0]:
#         x=v[0][0]

#     if v[1][1]==v[0][1]:
#         y=v[2][1]
#     else:   # if v[1][1]==v[2][1]:
#         y=v[0][1]


#     return [x,y]


# print(solution(lst))

# 비트 연산을 통해 불일치 판단 가능
def solution(v):
    x = v[0][0] ^ v[1][0] ^ v[2][0]
    y = v[0][1] ^ v[1][1] ^ v[2][1]
    return [x, y]

print(solution(lst))