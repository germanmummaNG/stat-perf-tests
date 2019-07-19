from locust import HttpLocust, TaskSet, task

filter_value_whole_country: str = '824'
filter_value_male_and_female: str = '919'


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.open_dashboard_regional_statistics()

    def open_dashboard_regional_statistics(self):
        self.client.get("/dashboard/3")

    @task
    def get_regional_statistics_plot(self):
        self.client.get("/dashboard/3/widget/33?graphType=area&language=et")

    @task
    def get_regional_statistics_plot_with_single_filter(self):
        regional_filter_part: str = '203=' + filter_value_whole_country
        self.client.get('/dashboard/3/widget/33?' + regional_filter_part + '&graphType=area&language=et')

    @task
    def get_regional_statistics_plot_with_two_filters(self):
        regional_filter_part: str = '203=' + filter_value_whole_country
        gender_filter_part: str = '204=' + filter_value_male_and_female
        self.client.get(
            '/dashboard/3/widget/33?' + regional_filter_part + '&' + gender_filter_part + '&graphType=area&language=et')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 800
    max_wait = 1200
