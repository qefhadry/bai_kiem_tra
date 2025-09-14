list1 = input("nhap danh sach").split()
list2 = []
for i in list1:
    c = int(i)
    list2.append(c) 
list2.sort()
print(list2[len(list2)-1])
print(list2[0])