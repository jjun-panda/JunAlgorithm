absolutes = [4,7,12]
signs = [True,False,True]


def solution(absolutes, signs):
    answer = 0 
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer

def solution2(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if s:
            answer += a
        else:
            answer -= a

    return answer 



print(solution2(absolutes, signs))
