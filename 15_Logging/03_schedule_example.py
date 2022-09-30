
import datetime
import os
import schedule
pid = os.getpid()
print(pid)
def print_time():
    now = datetime.datetime.now().replace(microsecond=0)
    print(f"PID: {pid}, {now}")
    with open('time.txt', 'a') as data:
        data.write(f"PID: {pid}, {now}\n")

schedule.every(5).seconds.do(print_time)

while True:
    schedule.run_pending()