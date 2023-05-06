# s = ")()("
# stack = []
# for i in s :
# 	if i == "(": # "()" 열린괄호가 나올 때
# 		stack.append(i) # 열린괄호를 저장
# 	else: # ")" 닫힌괄호가 나올 때
# 		if stack == []: # stack이 비어있는 상황(열리지 않았는데 닫힘, 다 짝지었는데 닫힘이 또 들어옴)
# 			print(False)
# 			break
# 		else:
# 			stack.pop() # 리스트의 맨 끝 데이터 제거

# print(stack)
# if stack != []:
# 	print(False)
# else:
# 	print(True)

# # if not stack:
# # 	print(True)

def solution(s):
	stack = []
	for i in s :
		if i == "(": # "(" 열린괄호가 나올 때
			stack.append(i) # 열린괄호를 저장
		else: # ")" 닫힌괄호가 나올 때
			if stack == []: # stack이 비어있는 상황(열리지 않았는데 닫힘, 다 짝지었는데 닫힘이 또 들어옴)
				return False
			else:
				stack.pop() # 리스트의 맨 끝 데이터 제거

	if stack != []:
		return False
	else:
		return True


# ----------------------------------------------------------------
# 출력 확인 테스트
s = ")()())"
stack = []
j = 0
for i in s:
	if i == "(":
		j += 1
		stack.append(i)
		print(stack)
	else:
		j -= 1
		stack.append(i)
		print(stack)
	if j < 0:
		stack.append(i)
		break

if j == 0 :
	print(False)
else :
	print(True)

# 1안
def solution(s):
	j = 0
	for i in s:
		if i == "(":
			j += 1
			# stack.append(i)
			# print(stack)
		else:
			j -= 1
			# stack.append(i)
			# print(stack)
			# stack.pop()
		if j < 0:
			break
	return j == 0

# 2안
def solution(s):
	j = 0
	for i in s:
		if i == "(": # 열린 괄호
			j += 1
		else: # 닫힌 괄호
			j -= 1
		if j < 0: # 열린 괄호의 개수보다 닫힌 괄호의 개수가 더 많은 상황
			break
	return j == 0

# 3안: 삼항 연산자
def solution(s):
	j = 0
	for i in s:
		j = j + 1 if i == "(" else j - 1 if i==")" else j
		if j < 0: 
			break
	return j == 0