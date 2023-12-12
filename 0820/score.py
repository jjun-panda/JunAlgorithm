name = ["may", "kein", "kain", "rady"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    dicts = {}
    result = []
    for n, y in zip(name, yearning):
        dicts[n] = y

    print(dicts) # {'may': 5, 'kein': 10, 'kain': 1, 'rady': 3}

    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dicts: # O(1)
                score += dicts[photo[i][j]]

        result.append(score)

    print(result) # [16, 15, 6]
    return result

solution(name, yearning, photo)