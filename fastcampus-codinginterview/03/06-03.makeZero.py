# 숫자 리스트 연산자 리스트를 분리
# 숫자와 리스트를 결합하여 나올 수 있는 경우의 수(연산자 리스트의 경우의 수) : 3^(n -1)
# 나오는 식을 계산하는 데 걸리는 시간은 최대 3^(9 - 1) 30000 미만 (문제에서 N은 최대 9라고 함)
# 모든 경우의 수를 게산할 때 재귀 쓸 수 있다.

# eval() 문자열 계산

import copy

# 어래이를 이렇게 쓰면 분기 가능
# 수 리스트의 크기가 n 이면 연산자는 n -1 개까지 가능
def recursive(array, n):
    if len(array) == n:
        # 길이가 2인 연산자 리스트 만들었을 때 list 에 넣겠다.
        # 파이썬 에서는 array를 공유함(shallow copy 로 추정). deepcopy 안하면 마지막에는 빈 리스트 나옴. 다 pop 했으니
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

    test_case = int(input())

    for _ in range(test_case):
        operators_list = []
        n = int(input())
        # 가능한 연산자의 조합 가능함
        recursive([], n - 1)

        # 숫자가 n 이었으면 0 ~ n - 1 까지 만들기
        integers = [i for i in range(1, n + 1)]

        # 숫자 리스트 사이에 연산자를 끼워넣기
        for operators_list in operators_list:
            string = ""
            for i in range(n - 1):
                # 1, 2, 3   // + -
                string += str(integers[i]) + operators[i]
            string += str(integers[-1]) # 마지막 3
            # 공백제거 후 계산(문제에서는 공백이면 그냥 연결하는 거니까 )
            if eval(string.replace(" ", "")) == 0:
                print(string)
        print()


