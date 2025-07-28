# import threading
# condition=threading.Condition()
 
# def my_thread():
#      with condition:
#       print("Thread signal is waiting")
#       condition.wait()
#       print("Thread signal is received")
     
# t = threading.Thread(target=my_thread)
# t.start()
# #t.join() #it doesn't print the next line of codes where it is notify is used or not

# with condition:
#     print('Signal is send')
#     condition.notify()
    
# t.join() #it print the all the codes

#Using Queue
#put()
#get()
# import threading
# import queue
# q=queue.Queue()

# def my_thread():
#     data=q.get()
#     print(f"Thread received dat,{data}")
#     q.task_done()
    
# t=threading.Thread(target=my_thread)
# t.start()

# q.put("Hello")
# q.put("WORLD")

# t.join()

#Using Daemon  (It is background process it runs infinite times when it is True)
import threading
import time

def my_thread():
    while True:
      print("Daemon thread is running")
      time.sleep(1)
t=threading.Thread(target=my_thread)
t.daemon=True
t.start()
t.join()