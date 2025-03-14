numbers = list(map(int, input("Nhập các số nguyên: ").split()))
unique_numbers = sorted(set(numbers), reverse=True)
if len(unique_numbers) < 2:
    print("Không có đủ hai số khác nhau.")
else:
    print("Số lớn thứ hai là:", unique_numbers[1])
