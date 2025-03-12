from datetime import datetime

from locust import  task, between, constant, HttpUser


class MyUser(HttpUser):

    wait_time = between(1,2)
    #wait_time = constant(2)
    #host = "https://www.google.com/"
    @task
    def demo(self):
        print(datetime.now())
        print("My name is Billa..!")


# How to run without UI
#  locust -f src/test_google.py -u 1 -r 1  --host "https://www.google.com/"