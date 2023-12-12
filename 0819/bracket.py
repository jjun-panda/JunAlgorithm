# -*- coding: utf-8 -*-

# 올바른 괄호 문자열인지 판단해주는 메소드
def bracket(s): 
    stack = [] 
    for b in s:
        if len(stack) == 0: stack.append(b)
        else:
            if b == ")" and stack[-1] == "(": stack.pop()
            elif b == "}" and stack[-1] == "{": stack.pop()
            elif b == "]" and stack[-1] == "[": stack.pop()
            else:
                stack.append(b) # 종류가 맞지 않거나 혹은 열린 괄호에 대해서는 stack에 저장 
        print("현재 문자열 ----> " ) 
        print(b)
        print("stack의 상태 --->")
        print(stack)

    if len(stack) == 0: return True
    else: return False 

s = "[)(]"
print(bracket(s))

def solution(s):
    answer = 0

    # 0 <= x < s의 길이 까지 회전
    for i in range(len(s)):
        #올바른 괄호문자열인지 판단 -> 올바르면, answer +=1 
        if bracket(s):
            answer += 1
        # 회전 
        s = s[1:] + s[0]

    return answer 