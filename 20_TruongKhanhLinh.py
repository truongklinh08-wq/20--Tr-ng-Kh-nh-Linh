def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if len(student_list) == 0:
        print("Danh sach trong.")
    else:
        for s in student_list:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
