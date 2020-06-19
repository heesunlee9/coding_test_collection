# https://www.acmicpc.net/problem/2750

# 1) selection sort : o(n^2)
# 2) python library : o(nlogn)
# 문제 조건에 data 가 1000 개 이므로 selection sort 로도 문제 없다.

# method1) - selection sort - 제일 작은 것 혹은 큰 앞으로 보내걸
n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

for i in range(n):
    min_index = i # 가장 작 원소의 인덱스
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

for i in array:
    print(i)

# method2)
# n = int(input())
# array = list()
#
# for _ in range(n):
#     array.append(int(input()))
#
# array.sort()
#
# for i in array:
#     print(i)


























