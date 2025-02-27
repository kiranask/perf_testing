from datetime import datetime

from locust import User, task, between, constant


class MyUser(User):

    #wait_time = between(1,2)
    wait_time = constant(2)
    @task
    def demo(self):
        print(datetime.now())
        print("My name is Billa..!")
