import threading
import time
def workload(task_id, scale_type, power=1):
    print(f"[{scale_type}] Task {task_id} starting with power {power}")
    result = 0
    for _ in range(1000000 * power):
        result += 1
    print(f"[{scale_type}] Task {task_id} completed")

def horizontal_scaling(num_threads=4):
    print("\n--- Horizontal Scaling Simulation ---")
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=workload, args=(i, "Horizontal"))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Horizontal scaling complete.\n")
def vertical_scaling(power=4):
    print("\n--- Vertical Scaling Simulation ---")
    threads = []
    t = threading.Thread(target=workload, args=(0, "Vertical", power))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    print("Vertical scaling complete.\n")
print("Resource Scaling Simulation (Horizontal vs Vertical)\n")
start = time.time()
horizontal_scaling(num_threads=4)
h_time = time.time() - start
start = time.time()
vertical_scaling(power=4)
v_time = time.time() - start
print(f"Time taken for Horizontal Scaling: {h_time:.2f} seconds")
print(f"Time taken for Vertical Scaling: {v_time:.2f} seconds")
