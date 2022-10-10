ne = int(input())
arr = map(int,input().split())
arr = list(arr)
cr = 0
ab = ""

 

for item in arr:
    cr = arr.count(item)
    if cr>1:
        for b in range(cr-1):
            ab = arr.index(item)
            arr.pop(ab)
    
leftovers = len(arr)
print(leftovers)
for item in arr:
    print(item,end=" ")
