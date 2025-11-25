import threading
import time
import random

class VirtualMachine: 
    def __init__(self, name):
        self.name = name
        self.cpu_usage = 0
        self.memory_usage = 0
        self.running = False

    def start(self):
        self.running = True
        print(f"[START] VM '{self.name}' is starting...")
        threading.Thread(target=self.monitor).start()

    def monitor(self):
        for i in range(5):
            if not self.running:
                break
            self.cpu_usage = random.randint(10, 90)
            self.memory_usage = random.randint(100, 500)
            print(f"[MONITOR] {self.name} - CPU: {self.cpu_usage}% | Memory: {self.memory_usage}MB")
            time.sleep(1)
        print(f"[STOP] VM '{self.name}' monitoring ended.\n")

    def stop(self):
        self.running = False
        print(f"[SHUTDOWN] VM '{self.name}' stopped.\n")

def main():
    vm1 = VirtualMachine("Ubuntu-VM")
    vm2 = VirtualMachine("Windows-VM")

    vm1.start()
    vm2.start()

    time.sleep(6)

    vm1.stop()
    vm2.stop()

if __name__ == "__main__":
    print("=== Virtual Machine Simulation ===\n")
    main()
