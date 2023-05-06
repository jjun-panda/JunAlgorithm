s = "banana"
word = list(s)
print(word)

def solution(s):
    answer = []
    s_dict = {}

    for idx, word in enumerate(list(s)):
        # s_dict에 word가 있을 시 (검색연산)
        if word in s_dict : # 0(1)
            answer.append(idx - s_dict[word]) # 거리계산
            s_dict[word] = idx # 위치정보 갱신(가장 마지막에 등장한 위치를 갱신한다)
        else :
            answer.append(-1) # 정답 배열에 -1 저장
            s_dict[word] = idx
    return answer

# answer = []
# s_dict = {}
# for idx, word in enumerate(list(s)):
#     # s_dict에 word가 있을 시 (검색연산)
#     if word in s_dict : # 0(1)
#         answer.append(idx - s_dict[word]) # 거리계산
#         s_dict[word] = idx # 위치정보 갱신(가장 마지막에 등장한 위치를 갱신한다)
#     else :
#         answer.append(-1) # 정답 배열에 -1 저장
#         s_dict[word] = idx
# print(answer)