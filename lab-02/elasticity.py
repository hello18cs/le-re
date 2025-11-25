import threading 
import time 
import queue 

def process_task(task_id):
    print("fProcessing Task {task_id}")
    time.sleep(1)
    print(f"Task {task_id} completed")

def worker(task_queue, thread_id):
    while True:
        try: 
            task_id = task_queue.get(timeout=2)
            print(f"[Thread-{thread_id}] picked Task-{task_id}")
            process_task(task_id)
            task_queue.task_done()
        except queue.Empty:
            print(f"[Thread-{thread_id}] no more tasks. Exiting....")
            break

def simulate_elasticity():
    task_queue = queue.Queue()

    for i in range(5):
        task_queue.put(i)
    num_threads = 2
    threads = []

    print("\nStarting with 2 worker threads....\n")

    for t_id in range(num_threads):
        t = threading.Thread(target=worker, args=(task_queue, t_id))
        t.start()
        threads.append(t)

    time.sleep(3)
    print("\nWorkload increased! Adding more tasks and more threads...\n")

    for i in range(5,15):
        task_queue.put(i)

    for t_id in range(2,5):
        t = threading.Thread(target=worker, args=(task_queue, t_id))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("\nAll tasks completed. Resources scaled elastically.\n")
simulate_elasticity()
