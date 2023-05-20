def solution() :
	solution() # 재귀(recursion) : 함수가 자기 자신을 호출 하는 것을 의미

# solution()

def countdown(num) :
	for i in range(num, -1, -1):
		print(i)

# countdown(10)

def countdown2(num):
	print(num)
	if num == 0:
		return
	countdown2(num-1)

# countdown2(10)


def factorial(num):
	if num == 1 : # 기저조건
		return
	else :
		return num * factorial(num-1)
