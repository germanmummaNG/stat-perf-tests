from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.getAllDashboards()

    def get_all_dashboards(self):
        self.client.get("/dashboard")

    @task
    def open_dashboard_regional_statistics(self):
        self.client.get("/dashboard/3")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 800
    max_wait = 1200
