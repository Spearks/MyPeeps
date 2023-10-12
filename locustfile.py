from locust import HttpUser, task
import random, string
import json


class UserFullTest(HttpUser):

    username = None
    password = None
    used_id = None
    token = None
    last_peep_id = None

    def on_start(self):

        # Generate random username
        self.username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))   

        # Fixed password
        self.password = "pass123"

        # Call user creation endpoint
        response = self.client.post("/api/v1/tests/createUser", json={
            "username": self.username,
            "password": self.password
        })

        # Check status code
        assert response.status_code == 200

        # Extract user ID from response
        response_data = response.json()
        user_id = response_data['user_id']

        # Assert user ID is returned
        self.user_id = user_id

        response = self.client.post("/api/v1/login", json={
            "username": self.username,
            "password": self.password
        })

        assert response.status_code == 200

        response_data = response.json()

        self.token = response_data["Token"]

    @task
    def get_peeps(self):
        # Add JWT authorization header
        headers = {"Authorization": f"Bearer {self.token}"}

        # Call peeps list endpoint 
        self.client.get("/api/v1/peeps", headers=headers)

    @task
    def create_peep(self):
        # Add JWT authorization header   
        headers = {"Authorization": f"Bearer {self.token}"}

        # Generate random peep name
        name = "".join(random.choices(string.ascii_lowercase, k=10))

        # Call peeps create endpoint
        response = self.client.post("/api/v1/peeps/", json={
           "name": name,
           "users" : [self.user_id]
        }, headers=headers)

        response_data = response.json()

        self.last_peep_id = response_data['id']


    @task
    def action_peep(self):

        headers = {"Authorization": f"Bearer {self.token}"}

        response = self.client.post("/api/v1/peeps/actions", json={
           "name": "Read",
           "options" : {
               "name" : "Read Pablo Neruda"
           },
           "peep" : self.last_peep_id
        }, headers=headers)