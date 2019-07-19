from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.open_dashboard_som()

    def open_dashboard_som(self):
        self.client.get("/dashboard/2")

    @task
    def get_png_from_screenshot_api(self):
        self.client.get("/screenshot?"
                        "dashboardId=2&"
                        "widgetId=9&"
                        "languageCode=et&"
                        "disableAnimation=true&"
                        "disableControls=true&"
                        "baseUrl=https%3A%2F%2Farendus.juhtimislauad.stat.ee%2Fbranches%2Fdevelop")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 800
    max_wait = 1200
