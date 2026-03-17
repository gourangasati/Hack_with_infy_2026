from collections import defaultdict
def food(A):
    n = len(A)
    pos = {}
    max_count = 0
    max_item = 0
    for i, item in enumerate(A):
        if item not in pos:
            pos[item] = []
        pos[item].append(i)
    for ite in pos:
        count = 0
        item = pos[ite]
        last = -2
        for val in item:
            if val - last > 1 :
                count += 1
                last = val
        if count > max_count :
            max_count = count
            max_item = ite
        if count == max_count:
            max_item = min(max_item , ite)
    return max_item
A = [0,2,3,2]
print(food(A))