#题目描述
#Write a Python function that computes the transpose of a given matrix.
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	return [list(row) for row in zip(*a)]
#这里zip的用法为
#zip按照索引依次提取多个可迭代对象中的元素，组合成为元组
#如果输入的可迭代对象长度不一致，zip 会以最短的为准
#eg：
# list1 = [1, 2, 3]
# list2 = ["a", "b", "c"]
# zipped = zip(list1, list2)
# print(list(zipped))  # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]
# list1 = [1, 2, 3]
# list2 = ["a", "b"]
# print(list(zip(list1, list2)))  # 输出: [(1, 'a'), (2, 'b')]