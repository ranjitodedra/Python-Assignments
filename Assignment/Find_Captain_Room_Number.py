N = int(input()) # members per group

list1 =map(int,input().split())  # room Number
list1 = sorted(list1)

for i in range(len(list1)): 
    if i!=len(list1)-1 :
        if list1[i]!=list1[i-1] and list1[i]!=list1[i+1] :
            print(list1[i])
    else:
        print(list1[i])