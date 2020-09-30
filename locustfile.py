from locust import HttpUser, TaskSet, task, between

domain_url = 'http://192.168.0.173:8000'
api_url = 'api_v0'

class QuickstartUesr(HttpUser):
    wait_time = between(1, 2)
    
    @task(1)
    def article_api_page(self):
        self.client.get('{0}/{1}/{2}/'.format(domain_url, api_url, 'articles'))