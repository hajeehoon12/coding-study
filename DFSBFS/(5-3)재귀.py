count = 0
def recursive_function(count):
    print('재귀 함수를 호출합니다.')
    count= count+1
    if count<10:
        recursive_function(count)

recursive_function(count)