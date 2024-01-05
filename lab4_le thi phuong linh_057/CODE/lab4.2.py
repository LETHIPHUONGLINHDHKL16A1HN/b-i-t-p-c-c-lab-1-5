import sqlite3
#tạo cơ sở dữ liệu và lưu vào thư mục data
def create_database_and_table():

    path = 'D:\Lê thị phương linh\lab4_le thi phuong linh_057\DATA'
    conn =sqlite3.connect(path)
    cursor = conn.cursor()

    create_table_query ="""
    CREATE TABLE IF NOT EXISTS product(
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close
    print("cơ sở dữ liệu và bảng đã đc tạo thành công")

#II viết các hàm cần thiết theo chức năng chương trình
def main_menu():
    while True:
        print("\n===menu quản lý sản phẩm===")
        print("1. tạo cơ sở dữ liệu và bảng")
        print("2.hiển thị danh sách sản phẩm")
        print("3.Thêm sản phẩm mới")
        print("4.tìm kiếm sản phẩm theo tên")
        print("5.cập nhật thông tin sản phẩm")
        print("6. xóa sản phẩm")
        print("7. thoát")

        choice = input("nhập lựa chọn của bạn từ 1-7:")

        if choice == '1':
            create_database_and_table()
        elif choice =='2':
            display_products()

        elif choice =='3':
            add_product_ui()
        elif choice =='4':
            pass
        elif choice =='5':
            pass
        elif choice =='6':
            pass
        elif choice =='7':
            print("thoát chương trình")
            break
        else:
            print("lựa chọn không hợp lệ. vui lòng nhập lại")
        
        #2 viết hàm nhận thông tin sản phẩm  

