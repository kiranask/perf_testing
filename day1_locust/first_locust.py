from locust import User, between, task

"""
locust -f FirstLocustFile.py


"""
class MyUser(User):
    wait_time = between(1, 2)

    @task
    def my_task1(self):
        print("task 1 executing")

    @task
    def my_task2(self):
        print("task 2 executing")