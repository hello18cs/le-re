import time
import random
import threading

class CloudInstance:
    """Simulates a cloud service instance (Primary/Backup)."""
    def __init__(self, name):
        self.name = name
        self.is_active = True  # health status

    def process_request(self, request_id):
        """Process request if instance is healthy."""
        if not self.is_active:
            raise Exception(f"{self.name} instance is DOWN in cloud!")
        print(f"{self.name} handled request {request_id}")

class CloudFailoverSystem:
    """Manages cloud failover between primary and backup."""
    def __init__(self, primary, backup):
        self.primary = primary
        self.backup = backup
        self.active_instance = primary
        self.lock = threading.Lock()

    def send_request(self, request_id):
        """Send request to active cloud instance."""
        with self.lock:
            try:
                self.active_instance.process_request(request_id)
            except Exception as e:
                print(f"Cloud Failure detected: {e}")
                self.failover()

                # Retry with the new active instance (likely backup)
                try:
                    self.active_instance.process_request(request_id)
                except Exception as e2:
                    print(f"Both cloud instances failed! Dropping request {request_id} ({e2})")

    def failover(self):
        """Switch traffic between cloud instances."""
        if self.active_instance == self.primary:
            print("Redirecting traffic to BACKUP cloud instance...")
            self.active_instance = self.backup
        else:
            print("Redirecting traffic back to PRIMARY cloud instance...")
            self.active_instance = self.primary

def client_requests(system, client_id, total=5):
    """Simulate client sending requests to the cloud."""
    for i in range(total):
        request_id = f"Client{client_id}-Req{i}"

        # Simulate random primary failure (~33% chance)
        if random.choice([True, False, False]):
            system.primary.is_active = False

        system.send_request(request_id)
        time.sleep(random.uniform(0.5, 1))

def cloud_health_monitor(system):
    """Background thread: restores primary after failure (simulates cloud self-healing)."""
    while True:
        time.sleep(1)
        if not system.primary.is_active:
            print("Cloud Monitor: Restoring PRIMARY instance...")
            system.primary.is_active = True

if __name__ == "__main__":
    # create cloud instances
    primary_instance = CloudInstance("PRIMARY")
    backup_instance = CloudInstance("BACKUP")
    system = CloudFailoverSystem(primary_instance, backup_instance)

    # start health monitor thread
    monitor_thread = threading.Thread(target=cloud_health_monitor, args=(system,), daemon=True)
    monitor_thread.start()

    # simulate multiple clients
    client_threads = []
    for cid in range(3):
        t = threading.Thread(target=client_requests, args=(system, cid))
        t.start()
        client_threads.append(t)

    for t in client_threads:
        t.join()

    print("✓ CLOUD FAILOVER SIMULATION COMPLETE")
