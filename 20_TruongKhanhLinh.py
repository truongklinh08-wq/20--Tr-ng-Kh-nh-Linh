def search_student(search_name):
    print("--- KET QUA TIM KIEM ---")
    found = False
    for s in student_list:
        if search_name.lower() in s['name'].lower():
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
            found = True
    if not found:
        print("Khong tim thay sinh vien nao.")

