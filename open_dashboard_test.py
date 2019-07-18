import random
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.getAllDashboards()
    
    def getAllDashboards(self):
        self.client.get("/dashboard")

    @task
    def openDashboardRegionalStatistics(self):
        self.client.get("/dashboard/3")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_function = lambda self: random.expovariate(1)*1000