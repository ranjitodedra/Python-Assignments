N = int(input()) #size of array

list1=map(int,input().split()) # scores 

list1 = sorted(list1)
new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

if len(new_list)>1:
    print(new_list[len(new_list)-2])