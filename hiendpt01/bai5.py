numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
unique_numbers = list(set(numbers))
print("Danh sách sau khi xóa các số trùng lặp:", unique_numbers)
