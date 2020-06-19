# https://www.acmicpc.net/problem/1302
# 어떤 원소가 나왔는지 아닌지 : set(), dictionary()
# 특히 개수를 셀 때 : dictionary()

n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values()) # 제일 많이 팔린거 해야 되니까
array = []

for book, number in books.items():
    if number == target:
        array.append(book)

print(sorted(array)[0]) # 제일 많이 팔린게 여러 개면 사전순으로 가장 앞서는 거