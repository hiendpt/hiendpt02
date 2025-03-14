numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
number_to_delete = int(input("Nhập số cần xóa khỏi danh sách: "))
if number_to_delete in numbers:
    numbers.remove(number_to_delete)
    print("Danh sách mới sau khi xóa:", numbers)
else:
    print("Số không có trong danh sách.")
