import random
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.openDashboardRegionalStatistics()
    
    def openDashboardRegionalStatistics(self):
        self.client.get("/dashboard/3")

    @task
    def openRegisteredUnemploymentBar(self):
        self.client.get("/dashboard/3/widget/33?graphType=bar&language=et")

    @task
    def openRegisteredUnemploymentArea(self):
        self.client.get("/dashboard/3/widget/33?graphType=area&language=et")

    @task
    def openRegisteredUnemploymentMap(self):
        self.client.get("/dashboard/3/widget/33?graphType=map&language=et")

    @task
    def openRegisteredUnemploymentVertical(self):
        self.client.get("/dashboard/3/widget/33?graphType=vertical&language=et")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_function = lambda self: random.expovariate(1)*1000