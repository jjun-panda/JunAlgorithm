def binary_search(array, value):
    # 먼저 찾으려는 값이 있을 수 있는 하향선, 상향선을 정한다.
    lower_bound = 0
    upper_bound = len(array) - 1

    # 상향선과 하향선 사이의 가운데 값을 계속 확인하는 반복문을 둔다.
    while lower_bound <= upper_bound :
        # 상향선과 하향선의 중간지점을 찾는다.
        midpoint = (lower_bound + upper_bound) // 2

        # 중간지점의 값을 확인한다.
        midvalue = array[midpoint]

        if midvalue == value : # 중간 지점의 값이 찾고있던 값이면, 검색 종료
            return midpoint
        elif midvalue > value: # 그렇지 않으면, 상향선 또는 하향선을 조정한다.
            upper_bound = midpoint - 1
        elif midvalue < value:
            lower_bound = midpoint + 1

    # 상향선과 하향선이 같아질 때까지 반복 완료 => 찾고 있는 값이 배열에 없다
    return lower_bound


# array = [202, 3, 75, 17, 80]
array = [3, 17, 75, 80, 202]
value = 22
print(binary_search(array, value))
