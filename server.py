import time
import threading
import task


time_interval=5 #default time unit: second

def command():
    while True:
        cmd = input()
        # write your reaction code for command here
        print("get commend:" + cmd)

def periodic(time_interval):
    last_time = int(time.time())
    while True:
        now_time = int(time.time())
        if now_time > last_time + time_interval:
            # print(time.localtime())
            task.main()
            last_time = int(time.time())

if __name__ == '__main__':
    thread1 = threading.Thread(name='scheduled_task', target=periodic, args=(time_interval,))
    thread1.start()
    print("Server started!")
    while True:
        command()
