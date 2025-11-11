customerid = [1 , 9, 49, 4 ,16 ,36 ,25 ]
def linearsearch(customerlist , targetid):
    for i in range(len(customerlist)):
        if customerlist[i] == targetid:
            return True
    return False
def binarysearch(sortedlist,targetid):
    low = 0
    high = len(sortedlist) - 1
    
    while low <= high :
        mid = (low + high) // 2
        if sortedlist[mid] == targetid:
            return True
        elif sortedlist[mid] < targetid:
            low = mid + 1
        else:
            high = mid - 1
    return False
searchid= int(input("enter customer id to search:"))
foundlinear = linearsearch(customerid, searchid)
print("linear search: found" if foundlinear else "Linear search: not found")
sortedid=sorted(customerid)
foundbinary = binarysearch(sortedid,searchid)
print("binary search: found" if foundbinary else "binary search: not found")