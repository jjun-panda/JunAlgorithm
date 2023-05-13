from text3 import binary_search

def solution(citations):
    # 정렬
    citations.sort() # 원본배열을 정렬
    length = len(citations)

    i = 0
    h = 0
    while i <= length: # i => h값의 후보, h값을 찾을 때까지 length까지 반복
        # h 이상 인용된 논문의 수 -> element의 값이 h  dltkddlek -> 어떤 element가 h값 -> h값의 인덱스?
        cand = binary_search(citations, i)

        if((length-1) - cand + 1 >= i) :
            h = max(h, i) # 현재 후보와 기존후보 중 큰 값을 선택(최대값을 찾아야한다)
        
        i += 1
    
    return h
