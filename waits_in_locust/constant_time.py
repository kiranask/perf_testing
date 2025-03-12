from datetime import datetime

from locust import User, task, between, constant
"""
How to run: locust -f src/constant_time.py

Concepts: 
wait_time = constant(2) 

✅ Your Current Code (with constant(2)) Does:
Execute the task.
Wait exactly 2 seconds before executing the task again.
If the task takes 1 second, the total time per loop = 1s (task) + 2s (wait) = 3s.
If the task takes 3 seconds, total time = 3s + 2s = 5s.
So, task timing is not uniform ⇒ This is not constant pacing.


constant_pacing: To simulate a steady load pattern, where each user does something every X seconds, regardless of how long the task took



"""

class MyUser(User):

    #wait_time = between(1,2)
    wait_time = constant(2)
    @task
    def demo(self):
        print(datetime.now())
        print("My name is Billa..!")
