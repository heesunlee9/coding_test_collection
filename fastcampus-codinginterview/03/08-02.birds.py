# 등차수열은 O(N^2)
# 등차수열만큼 숫자(n)를 계속 빼주니까
# 이 문제는 대략 O(root n)

# trials = 0
# remainingBirds = int(input())
# second = 1
#
# while remainingBirds > 0:
#     if second > remainingBirds:
#         second = 1
#     remainingBirds -= second
#     second += 1
#     trials += 1
# print(trials)

n = int(input())
result = 0
k = 1

while n != 0: # !
    if k > n:
        k = 1 # !
    n -= k
    k += 1 # !
    result += 1
print(result)