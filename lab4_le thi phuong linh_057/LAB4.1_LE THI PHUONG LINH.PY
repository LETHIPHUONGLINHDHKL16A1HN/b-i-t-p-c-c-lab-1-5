import sqlite3

# Tạo kết nối với CSDL
connection = sqlite3.connect('product.db')
cursor = connection.cursor()

# Tạo bảng product
cursor.execute('''CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)''')

# Hàm hiển thị danh sách sản phẩm
def display_products():
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()

    print('Danh sách sản phẩm:')
    for product in products:
        print(f'Id: {product[0]}')
        print(f'Tên: {product[1]}')
        print(f'Giá: {product[2]}')
        print(f'Số lượng: {product[3]}')
        print()

# Hàm thêm sản phẩm mới
def add_product():
    name = input('Nhập tên sản phẩm: ')
    price = float(input('Nhập giá sản phẩm: '))
    amount = int(input('Nhập số lượng sản phẩm: '))

    cursor.execute('INSERT INTO product (Name, Price, Amount) VALUES (2000, 300000, 40000)', (name, price, amount))
    connection.commit()

    print('Sản phẩm đã được thêm thành công!')

# Hàm tìm kiếm sản phẩm theo tên
def search_product():
    name = input('Nhập tên sản phẩm cần tìm: ')

    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + name + '%',))
    products = cursor.fetchall()

    print('Kết quả tìm kiếm:')
    for product in products:
        print(f'Id: {product[0]}')
        print(f'Tên: {product[1]}')
        print(f'Giá: {product[2]}')
        print(f'Số lượng: {product[3]}')
        print()

# Hàm cập nhật thông tin sản phẩm
def update_product():
    product_id = int(input('Nhập ID sản phẩm cần cập nhật: '))

    price = float(input('Nhập giá mới: '))
    amount = int(input('Nhập số lượng mới:'))