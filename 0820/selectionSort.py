def selectionSort(l):
    for i in range(len(l)):  # 패스스루의 단위 
        minIdx = i 
        for j in range(i+1, len(l)):
            if l[j] < l[minIdx]:
                minIdx = j # 최솟값을 찾고, 최솟값이 들어있는 인덱스로 갱신 

        if i != minIdx: # 최솟값이 갱신이 되었다면, 교환 
            l[i], l[minIdx] = l[minIdx], l[i]
        
        print(l)
    return l

l = [4,2,7,1,3]
selectionSort(l)

        