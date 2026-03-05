def ratcounthouse(r,unit,arr,n):
    ramain_food = r*unit
    count=0
    for num in arr:
        ramain_food = ramain_food-num
        print(ramain_food)
        if ramain_food > 0:
            count+=1
        if ramain_food ==0:
            return -1
        if ramain_food < 0:
            count+= 1
            break
    if ramain_food > 0 :
        return 0

    return count
r =7
unit =2
n= 8
arr = [2 ,8, 3, 5 ,7 ,4 ,1 ,2]
print(ratcounthouse(r,unit,arr,n))