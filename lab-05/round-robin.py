class ServiceInstance:
    def __init__(self,name):
        self.name = name
        
    def handle_request(self,request_id):
        print(f"{self.name} is handling request {request_id}")

class RoundRobinLoadBalancer:
    def __init__(self, instances):
        self.instances = instances
        self.index = 0 

    def get_instance(self):
        instance = self.instances[self.index]
        self.index = (self.index + 1) % len(self.instances)
        return instance

    def handle_request(self,request_id):
        instance = self.get_instance()
        instance.handle_request(request_id)
if __name__ == "__main__":
    instances = [ServiceInstance("Service-1"),
                 ServiceInstance("Service-2"),
                 ServiceInstance("Service0-3")]
    lb = RoundRobinLoadBalancer(instances)
    for req in range(1,11):
        lb.handle_request(req)