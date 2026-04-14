import pandas as pd

# Đọc file CSV
df = pd.read_csv("student_performance_dirty.csv")

# Hiển thị 5 dòng đầu tiên
print("===== 5 dòng đầu tiên =====")
print(df.head())

# Kiểm tra thông tin dữ liệu và kiểu dữ liệu
print("\n===== Thông tin dữ liệu =====")
print(df.info())

# Đếm số giá trị thiếu ở từng cột
print("\n===== Số giá trị thiếu ở từng cột =====")
print(df.isna().sum())