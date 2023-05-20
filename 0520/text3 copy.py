
def divide(p):
	open_b = 0
	close_b = 0
	for i in range(len(p)):
		if p[i] == '(' :
			open_b += 1
		else:
			close_b += 1

		if open_b == close_b :
			u = p[0:i+1]
			v = p[i+1::]
			return u, v

def chk(s):
	j = 0
	for i in s:
		j = j + 1 if i == "(" else j - 1 if i==")" else j
		if j < 0: 
			break
	return j == 0
		
p = "(()))("
# u = "(())" v=")("

# v=")("
# u = ")(" v=""
# "()"
def solution(p) :
	# 1. 입력이 빈 문자열일 때, 빈 문자열 반환
	if p == '':
		return p
	
	# 2. 문자열 w를 u, v로 분리
	u, v = divide(p)

	# 3. 문자열 u가 올바른 괄호 문자열 이라면 문자열 v에 대해 1단계부터 다시 수행
	if chk(u):
		# 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환
		return u + solution(v)
	# 4. 문자열 u가 올바른 문자열이 아니라면 아래 과정을 수행
	else :
		# 4-1. 빈 문자열에 첫번째 문자로 '('붙인다
		answer = '('
		# 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행결과 문자열을 이어 붙인다
		answer += solution(v)
		# 4-3. ')'를 다시 붙인다.
		answer += ')'
		# 4-4. u의 첫번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호방향을 뒤집어서 뒤에 붙인다.
		for b in u[1:len(u)-1]: # 0번째, 마지막 인덱스 제외. 마지막일때: len(u)-1
			if b == '(':
				answer += ')'
			else:
				answer += '('
		# 4-5/ 생성된 문자열을 반환한다.
		return answer
print(solution(p))