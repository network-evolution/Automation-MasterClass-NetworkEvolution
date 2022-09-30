import subprocess
from datetime import datetime
import threading
start_time = datetime.now()
def ping_test(host, value):
    try:
        print(f"Started at {datetime.now()} for {host} \n")
        subprocess.check_output(["ping", f"-c{value}", f"{host}"])
        print(f"{datetime.now()} {host}- Reachable, Value: {value}")
    except subprocess.CalledProcessError:
        print(f"{datetime.now()} {host}- Not reachable, Value: {value}\n")

h1 = {'host': '192.168.0.1', 'value': 2}
h2 = {'host': '192.168.0.100', 'value': 2}

# ping_test(**h1)
# ping_test(**h2)

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

# for host in hosts:
#     ping_test(**host)

# th1 = threading.Thread(target=ping_test, kwargs=hosts[0])
# th2 = threading.Thread(target=ping_test, kwargs=hosts[1])
# print(th1)
# print(type(th1))
# print(dir(th1))
# th1.start()
# th2.start()
# th1.join()
# th2.join()
###########################################
ping_host_threads = []
for host in hosts:
    ping_thread = threading.Thread(target=ping_test, kwargs=host)
    ping_thread.start()
    ping_host_threads.append(ping_thread)
for thread in ping_host_threads:
    thread.join()

##############################################
end_time = datetime.now()
print(end_time - start_time)