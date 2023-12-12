def bubbleSort(l):
    idx = len(l) - 1 # 어떤 인덱스까지 아직 정렬되지 않았는지를 기록. 초기값: 배열의 마지막 인덱스 
    sorted = False # 배열의 정렬 여부 기록 

    while not sorted: # 배열이 정렬될 때까지 반복 
        sorted = True
        for i in range(idx): # 첫 인덱스부터 아직 정렬되지 않은 인덱스까지 반복 (passthrough의 단위)
            if l[i] > l[i+1]: # 왼쪽의 값이 오른쪽의 값보다 크면 교환 
                sorted = False
                l[i], l[i+1] = l[i+1], l[i] # 교환(swap)

        print(l)
        idx -= 1 # 패스스루가 한 번 끝났으면 버블이 올바른 위치에 있다고 확인 가능 

    return l

l = [4,2,7,1,3]
print(bubbleSort(l))

