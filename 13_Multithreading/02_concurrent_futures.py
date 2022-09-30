import subprocess
import time
from datetime import datetime
import concurrent.futures as cf

start_time = datetime.now()

def ping_test(host, value):
    try:
        print(f"Started at {datetime.now()} for {host} \n")
        subprocess.check_output(["ping", f"-c{value}", f"{host}"])
        # print(f"{datetime.now()} {host}- Reachable, Value: {value}")
        return f"{datetime.now()} {host}- Reachable, Value: {value}"
    except subprocess.CalledProcessError:
        # print(f"{datetime.now()} {host}- Not reachable, Value: {value}\n")
        return f"{datetime.now()} {host}- Not reachable, Value: {value}\n"

hosts = [{'host': '192.168.0.1', 'value': 2},
         {'host': '192.168.0.2', 'value': 2},
         {'host': '192.168.0.3', 'value': 2},
         {'host': '192.168.0.4', 'value': 2},
         {'host': '192.168.0.5', 'value': 2},
         {'host': '192.168.0.6', 'value': 2},
         {'host': '192.168.0.7', 'value': 2},
         {'host': '192.168.0.8', 'value': 2},
         {'host': '192.168.0.9', 'value': 2},
         {'host': '192.168.0.10', 'value': 2},
         ]

# with cf.ThreadPoolExecutor() as executor:
#     c1 = executor.submit(ping_test, **hosts[0])
#     print(c1)
#     print(type(c1))
#     print(dir(c1))
#     print(c1.running())
#     time.sleep(3)
#     print(c1.running())


# total_output = []
# with cf.ThreadPoolExecutor() as executor:
#     for host in hosts:
#         output = executor.submit(ping_test, **host)
#         total_output.append(output)
#     for f in cf.as_completed(total_output):
#         print(f.result())


with cf.ThreadPoolExecutor() as executor:
    total_output = [executor.submit(ping_test, **host) for host in hosts]
    # for f in cf.as_completed(total_output):
    #     print(f.result())





##############################################
end_time = datetime.now()
print(end_time - start_time)