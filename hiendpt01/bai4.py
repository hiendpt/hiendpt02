numbers = list(map(int, input("Nhập các số nguyên: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
print("Danh sách chỉ chứa các số chẵn:", even_numbers)
