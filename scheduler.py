# Import modules

import schedule
import time

# Schedule tasks
def schedule_job(job):
    schedule.every(1).day.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


