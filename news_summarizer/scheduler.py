# Import modules
import schedule
import time # Time module for sleep functionality

# Schedule tasks
def schedule_job(send_time, job):
    schedule.every(1).day.at(send_time).do(job) # Set daily job schedule

    while True:
        schedule.run_pending() # Execute task
        time.sleep(1)
