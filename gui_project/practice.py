kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

a = list(zip(kor, eng))
print(a)

b = list(zip(*a))

print(b)
