# 06. 재귀호출 - 핵심유형

# 점화식을 세울 수 있으면 재귀로 풀릴 가능성이 있다.
# 내 답
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))
# 구할 수는 있는데 시간초 나옴
# O(2^n) : 너무 오래 걸려 2 * 45 면 10억 이상

# 재귀 문제점 : 동일한 내용이 계속 호출됨(f(1))
# 대안 : dynamic programming 또는 반복문

n = int(input())
a, b = 0, 1
while n > 0:
    a, b = b, a + b
    n -= 1
print(a)