import threading
import time
lock1=threading.Lock()
lock2=threading.Lock()
def task1():
    lock1.acquire()
    print('Task1 is locked by lock1')
    lock2.acquire()
    print('Task1 is locked by lock2')
    
    print("Task 1 is started")
    time.sleep(2)
    print("Task 1 is completed")
    lock1.release()
    lock2.release()
    
def task2():
    lock2.acquire()
    print('Task2 is locked by lock1')
    lock1.acquire()
    print('Task2 is locked by lock2')
    
    print("Task 2 is started")
    time.sleep(5)
    print("Task 2 is completed")
    lock2.release()
    lock1.release()
    
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
print("All the task is completed")