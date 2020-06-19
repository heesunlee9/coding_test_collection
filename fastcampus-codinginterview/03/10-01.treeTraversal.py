# https://www.acmicpc.net/problem/1991
# 자료구조 자체 구현 문제, 구현 묻는 문제. 자료구조 자체를 구현할 때는 실수 가능. 주의
# 트리는 재귀로 구현하는 경우 많다.

# 중위 : 가로축을 기준으로 했을 때 왼쪽에서 오른쪽 순으로 나온다. (문제 출제 가능)
# 구축 -> 순회
# 시간복잡도는 안 복잡한데 구현이 까다로움


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.left_node = right_node

def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')


n = int(input())
tree = {} # 간단하게 만들어야 하거나 DB 용량이 적을 때 dict 사용 가능
for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
