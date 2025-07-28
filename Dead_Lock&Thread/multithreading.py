#Multithreading

# import threading
#
# def my_func(args1,args2):
#     print("Function is running",args1,args2)
#
# t=threading.Thread(target=my_func,args=(1,2))
# t.start()
# t.join()
# print("Thread is completed")

# import threading
# import time
# def task1():
#     print('Task1 is started')
#     time.sleep(5)
#     print('Task1 is completed')
# def task2():
#     print('Task2 is started')
#     time.sleep(5)
#     print('Task2 is completed')
# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("all task is completed")

# from  concurrent.futures import ThreadPoolExecutor
# import time
# def task1():
#     print('Task1 is started')
#     time.sleep(5)
#     print('Task1 is completed')
#     return 'task1'
# def task2():
#     print('Task2 is started')
#     time.sleep(5)
#     print('Task2 is completed')
#     return 'task2'
# with ThreadPoolExecutor(max_workers=2) as executor:
#     task1_futures=executor.submit(task1)
#     task2_futures=executor.submit(task2)
#
# task1_result=task1_futures.result()
# task2_result=task2_futures.result()
#
# print("All task is completed")

#Locks and Semaphores

#Lock # This is used to prevent the deadlock situation
# import threading
# import time
# lock=threading.Lock()
# def task1():
#     #acquire lock
#     lock.acquire()
#     print('Task1 is started')
#     time.sleep(2)
#     print('Task1 is completed')
#     #lock release
#     lock.release()
# def task2():
#     lock.acquire()
#     print('Task2 is started')
#     time.sleep(3)
#     print('Task2 is completed')
#     lock.release()
# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("all task is completed")

#Semaphores # This is used to limit the number of threads that can access a resource at the same time
# import threading
# import time
# semaphore=threading.Semaphore(2)
# def task1():
#     #acquire lock
#     semaphore.acquire()
#     print('Task1 is started')
#     time.sleep(2)
#     print('Task1 is completed')
#     #lock release
#     semaphore.release()
# def task2():
#     semaphore.acquire()
#     print('Task2 is started')
#     time.sleep(3)
#     print('Task2 is completed')
#     semaphore.release()
#
# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("all task is completed")