ten = input("nhap ho ten:").split()
print(ten)
a = ten[0]
b = ten[len(ten)-1]
ten.remove(ten[0])
ten.remove(ten[len(ten)-1])
c =""
for i in ten:
    c += " " + i 
print(f"ten : {b}")
print(f"ten dem : {c}")
print(f"ho : {a}")
