import psutil
import time

def monitor_resources(interval=2):
    print("Cloud Resource Monitoring Simulation\n")
    print("Press Ctrl+C to stop monitoring...\n")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory.percent}% (Used: {memory.used // (1024 ** 2)} MB / Total: {memory.total // (1024 ** 2)} MB)")
            print(f"Disk Usage: {disk.percent}% (Used: {disk.used // (1024 ** 3)} GB / Total: {disk.total // (1024 ** 3)} GB)")
            print("-" * 40)
            
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor_resources(interval=3)
#& "c:\Program Files\Python385\python.exe" -m pip install psutil
#python resource_monitor.py
