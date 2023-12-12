def insertionSort(l):
    for i in range(1, len(l)): # 인덱스 1부터 시작 
        tmp = l[i] # 현재값 저장 # 삭제 
        idx = i # 현재 인덱스 저장 

        while idx > 0 and l[idx-1] > tmp: #공백이 배열 왼쪽 끝에 도달하거나 공백 왼쪽에 있는 값이 tmp보다 작을때까지 반복 # 비교
            l[idx] = l[idx-1] #왼쪽 값을 한 셀 오른쪽으로 시프트 # 시프트 
            idx -= 1 # 공백의 위치 갱신 

        l[idx] = tmp 
        print(l)

    return l 

l = [4,2,7,1,3]
insertionSort(l)