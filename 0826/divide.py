

def divide(left_pointer, right_pointer):
    # 피벗 선택 
    pivot_position = right_pointer
    pivot = array[pivot_position]

    right_pointer = pivot_position - 1

    while True: # 두 포인터가 가리키는 값이 같아질 때까지 반복 

        # 왼쪽 포인터를 한 셀씩 계속 오른쪽으로 옮기면서 피벗보다 크거나 같은 닶에 도달하면 멈춤 
        while array[left_pointer]  < pivot:
            left_pointer += 1

        # 오른쪽 포인터를 한 셀씩 계속 왼쪽으로 옮기면서 피벗보다 작거나 같은 값에 도달하면 멈춤 
        while array[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break
        else:
            # 왼쪽 포인터 값과 오른쪽 포인터의 값을˜ 교환한다 
            swap(left_pointer, right_pointer)

    # 왼쪽 포인터가 가리키고 있는 값과 피벗을 교환한다 
    swap(left_pointer, pivot_position)
    return left_pointer # 분할이 끝난 후 피벗의 위치 

def swap(left_idx, right_idx):
    array[left_idx], array[right_idx] = array[right_idx], array[left_idx]

array = [0,5,2,1,6,3]
divide(0, len(array)-1)
print(array) # [0, 1, 2, 3, 6, 5]


def quickSort(left_idx, right_idx):
    # 기저조건(함수가 자기자신을 호출하지 않는 조건): 하위 배열의 원소의 개수가 1개 이하 
    if right_idx <= left_idx:
        return

    # 배열을 분할하고 피벗의 위치를 가져옴 
    pivot_position = divide(left_idx, right_idx)

    # 피벗의 왼쪽에 대해 재귀적으로 호출 
    quickSort(left_idx, pivot_position-1)

    # 피벗의 오른쪽에 대해 재귀적으로 호출 
    quickSort(pivot_position+1, right_idx)

array = [0,5,2,1,6,3]
quickSort(0, len(array)-1)
print(array) # [0, 1, 2, 3, 5, 6]

# q) 배열 내에서 k번째로 작은 값? 
def quickSelect(kth_lowest_value, left_idx, right_idx) :
    if right_idx <= left_idx:
        return array[left_idx]

    # 배열을 분할하고 피벗의 위치를 가져옴
    pivot_position = divide(left_idx, right_idx)

    if kth_lowest_value < pivot_position:
        # 피벗의 위치에서 왼쪽을 분할 
        quickSelect(kth_lowest_value, left_idx, pivot_position-1)
    elif kth_lowest_value > pivot_position:
        # 피벗의 위치에서 오른쪽을 분할 
        quickSelect(kth_lowest_value, pivot_position+1, right_idx)
    else:
        # 피벗의 위치와 k번째 작은 값의 위치가 동일 
        print(pivot_position, array[pivot_position])
        return array[pivot_position]

array = [0,50,20,10,60,30]
quickSelect(2, 0, len(array)-1) # 2, 20 -> 2: 인덱스값 => 3번째로 작은값 