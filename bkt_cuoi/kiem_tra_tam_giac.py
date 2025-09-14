

a = float(input("nhap canh a:"))
b = float(input("nhap canh b:"))
c = float(input("nhap canh c:"))


if ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("khong phai tam giac")
elif a == b == c :
    print("tam giac deu")
elif a == b or a==c or c==b:
    print("tam giac can")
elif ((a**2 + b**2) == c**2) or ((a**2 + c**2) == b**2) or ((c**2 + b**2) == a**2) :
    print("tam giac vuong")
else :
    print("tam giac thuong")

