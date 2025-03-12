from datetime import datetime
import time
from locust import User, task

"""

🧠 How Constant Pacing Works (Concept):
Let’s say:

You want each iteration to take exactly 5 seconds.
Your task (e.g., HTTP request) takes 2 seconds.
Then:

Constant pacing = Run the task (2s) → then wait (3s) = total 5s.
If the task takes 4s, wait = 1s.
If the task takes 6s (more than pacing target), wait = 0s (no negative wait).


"""

class MyUser(User):
    pacing_time = 5  # seconds

    @task
    def demo(self):
        start_time = time.time()

        print(datetime.now())
        print("My name is Billa..!")

        elapsed = time.time() - start_time
        sleep_time = max(0, self.pacing_time - elapsed)
        time.sleep(sleep_time)
