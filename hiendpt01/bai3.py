numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
number_to_check = int(input("Nhập số cần kiểm tra: "))
count = numbers.count(number_to_check)
print(f"Số {number_to_check} xuất hiện {count} lần trong danh sách.")
