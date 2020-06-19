# 트리의 높이와 너비
# https://www.acmicpc.net/problem/2250
# 중위 순회를 이용하면 X축을 기준으로 왼쪽부터 방문한다는 특징 있다. + level 값 저장
# 중위 순회 하니까 너비 구하는 데 용이함
# 트리를 만들기 - 트리 탐색
# 시간복잡도는 안 복잡한데 구현이 까다로움


class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1 # 1번 노드가 root 노드가 아닐 수도 있다. # parent 가 -1 이라는 건 부모없다. 즉 루트 노드라는 거임
        self.number = number
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    # 왼쪽 노드 방문
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    # 데이터 처리
    level_min[level] = min(level_min[level], x) # 각 레벨의 작은거 구하기(
    level_max[level] = max(level_max[level], x) # 큰 거 구하기(나중에 빼려고)
    x += 1
    # 오른쪽 노드 방문
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)

# 트리 만들기
n = int(input())
tree = {}
level_min = [n] # 일단 가장 크게
level_max = [0]
root = -1
x = 1
level_depth = 1

## 초기화
for i in range(1, n + 1): # 루트는 방문해서 + 1
    tree[i] = Node(i, -1, -1)
    level_min.append(n) # 일단 각각의 레벨이 노드 개수 만큼 되게 하기
    level_max.append(0)

for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    # 부모자식 이어주기 - 값 넣기
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    # 부모 자식 이어주기 - 링크 연결
    if left_node != -1: # 왼쪽 자식 존재 할 때
        tree[left_node].parent = number # 부모 찾기
    if right_node != -1:
        tree[right_node].parent = number

for i in range(1, n + 1):
    # 부모 노드가 없는 트리가 부모 노드라고 가정
    if tree[i].parent == -1:
        root = i

# 순회하기 + 레벨 기록
in_order(tree[root], 1) # 루트 빼고 레벨 1 부터 시작

# width 알아내기
result_level = 1
result_width = level_max[1] - level_min[1] + 1 # level1 의 width 계산
for i in range(2, level_depth + 1): # 모든 레벨 돌면서
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i # 갱신
        result_width = width

print(result_level, result_width)


