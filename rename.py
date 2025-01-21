import os
import uuid

def rename_images_in_directory(directory):
    # ตรวจสอบว่าดirectory ที่ระบุมีอยู่จริง
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # ตรวจสอบไฟล์ทั้งหมดใน directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # ตรวจสอบว่าเป็นไฟล์
        if os.path.isfile(file_path):
            # ดึงนามสกุลไฟล์ (เช่น .jpg, .png)
            _, ext = os.path.splitext(filename)

            # สร้างชื่อใหม่แบบสุ่ม
            new_name = f"{uuid.uuid4()}{ext}"

            # เปลี่ยนชื่อไฟล์
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

# ระบุ path ของ directory ที่เก็บไฟล์รูปภาพ
directory_path = r"C:\Users\satit\Desktop\D\N_true"

# เรียกใช้งานฟังก์ชัน
rename_images_in_directory(directory_path)
