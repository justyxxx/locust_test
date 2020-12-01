from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    @task(2)
    def posts(self):
        self.client.get("/posts")

    @task(1)
    def comment(self):
        data = {
            "postId": 1,
            "name": "comment",
            "email": "qwerty@gmai.com",
            "body": "Lorem ipsum"
        }
        self.client.post("/comments", data)


class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    min_wait = 1000
    max_wait = 3000
