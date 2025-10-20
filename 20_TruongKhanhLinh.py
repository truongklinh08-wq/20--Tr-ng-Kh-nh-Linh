# student_manager.py
# Họ tên: Trương Khánh Linh – MSSV: 20

student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1:
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh vien <ten> thanh cong."
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")
