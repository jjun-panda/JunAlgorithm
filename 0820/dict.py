s = "23four5six7"
def solution(s):
    dicts = {"0": "zero", "1":"one", "2":"two", "3":"three", "4":"four", 
            "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}

    result = s
    for k, v in dicts.items():
        result = result.replace(v, k)
        
    return int(result)

print(solution(s))




dicts = {"0": "zero", "1":"one", "2":"two", "3":"three", "4":"four", 
            "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}

print(dicts)
print(dicts.keys()) # dict_keys(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print(dicts.values()) #dict_values(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
print(dicts.items()) 
# dict_items([('0', 'zero'), ('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five'), ('6', 'six'), ('7', 'seven'), ('8', 'eight'), ('9', 'nine')]
    
