#1
import threading
import time
class SimpleTask:
 def run_task(self):
    for i in range(1, 4):
        print('Đã in lần thứ :',i)
 time.sleep(1)

def main():
 # Tạo và khởi chạy nhiều threads
 tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
 for task in tasks:
    task.start()
 for task in tasks:
    task.join()
if __name__ == "__main__":
 main() 

#2
class SimpleTask:
 def run_task(self):
    global counter
 for _ in range(4):
        time.sleep(2)
 counter += 1 # Tăng counter mà không sử dụng lock
 print(f"Counter đã tăng lên: {counter}")
def main():
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)] #tạo 1 luồng đơn và nhân thành nhiều luồng
    
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
if __name__ == "__main__":
 main() 


#3
import threading
import time
counter = 0
counter_lock = threading.Lock()
class SimpleTask:
 def run_task(self):
    global counter
 for _ in range(3):
    time.sleep(2)
 with counter_lock:
    counter += 1
 print(f"Counter đã tăng lên: {counter}")
def main():
 tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
 for task in tasks:
    task.start()
 for task in tasks:
    task.join()
if __name__ == "__main__":
 main()
