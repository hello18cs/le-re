import requests
import time

service_endpoints = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.openai.com"
]

SLA_THRESHOLD = 0.8  # response time threshold in seconds

print("----- SLA Monitoring Started -----\n")

for service in service_endpoints:
    try:
        start_time = time.time()
        response = requests.get(service)
        end_time = time.time()

        response_time = end_time - start_time

        print(f"Service: {service}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.3f} sec")

        if response_time <= SLA_THRESHOLD:
            print("SLA Met\n")
        else:
            print("SLA Breached\n")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {service}: {e}\n")

print("----- SLA Monitoring Completed -----")
