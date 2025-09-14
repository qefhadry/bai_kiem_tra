def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def kiem_tra_ngay(d, m, y):
    # Kiểm tra tháng hợp lệ
    if m < 1 or m > 12:
        return False

    # Số ngày tối đa theo tháng
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif m in [4, 6, 9, 11]:
        max_day = 30
    else:  # Tháng 2
        if la_nam_nhuan(y):
            max_day = 29
        else:
            max_day = 28

    # Kiểm tra ngày hợp lệ
    return 1 <= d <= max_day

def main():
    date_str = input("Nhập ngày theo định dạng dd/mm/yyyy: ")
    try:
        d, m, y = map(int, date_str.split("/"))
        if kiem_tra_ngay(d, m, y):
            print("Ngày hợp lệ!")
        else:
            print("Ngày không hợp lệ!")
    except:
        print("Định dạng không đúng! Hãy nhập dd/mm/yyyy")

# Chạy chương trình
main()
