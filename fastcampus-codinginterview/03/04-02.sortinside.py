# https://www.acmicpc.net/problem/1427

array = input()

# 자리 수로 쪼개서 리스트에 넣기
for i in range(9, -1, -1): # 0~9 돌아가면서 자리수 몇 개 있는지 세기
    for j in array:
        if int(j) == i:
            print(i, end='')
# o(n^2)





















