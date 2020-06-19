# O(문서의 길이 * 단어의 길이) : 최대 십만

document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index : index + len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)


