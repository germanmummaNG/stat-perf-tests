from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.open_dashboard_regional_statistics()

    def open_dashboard_regional_statistics(self):
        self.client.get("/dashboard/3")

    @task
    def open_registered_unemployment_bar(self):
        self.client.get("/dashboard/3/widget/33?graphType=bar&language=et")

    @task
    def open_registered_unemployment_area(self):
        self.client.get("/dashboard/3/widget/33?graphType=area&language=et")

    @task
    def open_registered_unemployment_map(self):
        self.client.get("/dashboard/3/widget/33?graphType=map&language=et")

    @task
    def open_registered_unemployment_vertical(self):
        self.client.get("/dashboard/3/widget/33?graphType=vertical&language=et")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 800
    max_wait = 1200
