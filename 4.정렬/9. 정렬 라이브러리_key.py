array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

# key에 함수 입력
result = sorted(array, key=setting)
print(result)
