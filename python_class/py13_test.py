'''# ------ page. 54 ------
# --- 使用subprocess建立一個程序
import subprocess, time

calcproc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# 監控subprocess是否正常開啟
while True:
    print(calcproc.poll())
    if calcproc.poll() != None:
        print('小算盤已開啟')
        break

# 暫停5秒
time.sleep(5)

# 結束小算盤程序
proc = subprocess.Popen("Taskkill /IM Calculator.exe /F")
'''
'''# ------ page. 55 ------
# --- 多行程運算範例
import multiprocessing as mp
import os, random, time

def pm(task_id, task_queue):
    task = [0, '']
    task_type = random.sample(['Level A Task', 'Level B Task', 'Level C Task', 'Level S Task'], k=1)
    task[0] = task_id; task[1] = task_type
    print('PM 接到了一項', task[1], '編號', task[0])
    task_queue.put(task)

def worker(worker_id, task_queue):
    while True:
        task = list(task_queue.get())
        time.sleep(random.randrange(2))
        print('worker', worker_id, '處理了一項', task[1], '編號', task[0], 'PID =', os.getpid())
        task_queue.task_done()

def main():
    task_queue = mp.JoinableQueue()

    worker1 = mp.Process(target=worker,args=(1,task_queue))
    worker1.daemon = True
    worker1.start()

    worker2 = mp.Process(target=worker, args=(2, task_queue))
    worker2.daemon = True
    worker2.start()

    for id in range(100):
        pm(id, task_queue)
    task_queue.join()


if __name__ == "__main__":
    main()

print()'''
# ------ page. 56 ------
# --- 多執行緒範例
import threading, queue
import os, random, time

def pm(task_id, task_queue):
    task = [0, '']
    task_type = random.sample(['task A', 'task B', 'task C', 'task D', ], k=1)
    task[0] = task_id; task[1] = task_type
    print('PM接到了一項', [1], '編號', task[0])
    task_queue.put(task)

def worker(worker_id, task_queue):
    while True:
        task = list(task_queue.get())
        time.sleep(random.randrange(2))
        print('worker', worker_id, '處理了一項', task[1], '編號', task[0], 'PID=', os.getpid())
        task_queue.task_done()

def main():
    task_queue = queue.Queue()

    worker1 = threading.Thread(target=worker, args=(1,task_queue))
    worker1.start()

    worker2 = threading.Thread(target=worker, args=(2, task_queue))
    worker2.start()

    for id in range(100):
        pm(id, task_queue)
    task_queue.join()

if __name__ == "__main__":
    main()









