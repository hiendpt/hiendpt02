numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
total = sum(numbers)
average = total / len(numbers) if len(numbers) > 0 else 0
print("Tổng các phần tử:", total)
print("Trung bình các phần tử:", average)
