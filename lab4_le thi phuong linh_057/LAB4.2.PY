import sqlite3

# Kết nối đến CSDL
connection = sqlite3.connect('product.db')

# Khởi tạo con trỏ cho CSDL
cursor = connection.cursor()

# Tạo bảng `product`
cursor.execute("""CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)""")

# Xây dựng menu giao diện
while True:
    print("\n--- Hệ thống quản lý sản phẩm ---")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Tìm kiếm sản phẩm theo tên")
    print("4. Cập nhật thông tin sản phẩm")
    print("5. Xóa sản phẩm")
    print("6. Thoát")
    choice = input("Lựa chọn của bạn: ")

    # Xử lý lựa chọn của người dùng
    if choice == "1":
        # Hiển thị danh sách sản phẩm
        cursor.execute("SELECT * FROM product")
        results = cursor.fetchall()
        print("\nDanh sách sản phẩm:")
        for product in results:
            print(f"ID: {product[0]} - Tên: {product[1]} - Giá: {product[2]} - Số lượng: {product[3]}")

    elif choice == "2":
        # Thêm sản phẩm mới
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá sản phẩm: "))
        amount = int(input("Nhập số lượng sản phẩm: "))
        cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
        connection.commit()
        print("Thêm sản phẩm thành công!")

    elif choice == "3":

        # Tìm kiếm sản phẩm theo tên
        name = input("Nhập tên sản phẩm cần tìm: ")
        cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
        results = cursor.fetchall()
        if results:
            print(f"\nKết quả tìm kiếm cho '{name}':)