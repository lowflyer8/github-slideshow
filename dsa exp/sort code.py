salary=[49000,64000,81000,100000,121000,144000,169000,196000]
def selectionsort(salarylist):
    n=len(salarylist)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if salarylist[j]<salarylist[minindex]:
                minindex=j
        salarylist[i],salarylist[minindex]=salarylist[minindex],salarylist[i]
    return salarylist
def bubblesort(salarylist):
    n=len(salarylist)
    for i in range(n):
        for j in range(0,n-i-1):
            if salarylist[j]>salarylist[j+1]:
                salarylist[j],salarylist[j+1]=salarylist[j+1],salarylist[j]
    return salarylist
sortedsalaryselection = selectionsort(salary.copy())
print("top 5 salary (selection sort):",sortedsalaryselection[ -5:][::-1])
sortedsalarybubble = bubblesort(salary.copy())
print("top 5 salary (bubble sort):",sortedsalarybubble[-5:][::-1])