#2. Sử dụng OOP thực hiện bài Tập: Đọc và Hiển Thị Dữ Liệu từ Tập Tin JSON.
#Các Bước Thực Hiện
#1. Chuẩn Bị Tập Tin JSON (5 phút):
#Tạo một tập tin JSON đơn giản có chứa thông tin người dùng (ví dụ: tên, tuổi, địa chỉ). Có
#thể tạo tập tin này sử dụng một trình soạn thảo văn bản và lưu với đuôi .json.
#Ví dụ nội dung tập tin users.json:
[
{"name": "Nguyen Van A", "age": 30, "address": "Hanoi"},
{"name": "Tran Thi B", "age": 25, "address": "HCM City"}
]
#2. Đọc Tập Tin JSON Trong Python:
# Viết một script Python để mở và đọc tập tin JSON.
# Sử dụng thư viện json có sẵn trong Python.


import json
class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, \Address:{user['address']}")
# Sử dụng lớp JSONReader
path = 'D:\Lê thị phương linh\16A1KHDL\DATA\products.xml'
reader = JSONReader(path)
reader.read_json()
reader.display_data()