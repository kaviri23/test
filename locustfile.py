from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # simulated users wait 1-3 seconds between tasks

    @task
    def load_homepage(self):
        self.client.get("/")

# --- Test parameters defined directly in the script ---
if __name__ == "__main__":
    import subprocess

    TARGET_HOST = "https://example.com"   # placeholder for now
    NUM_USERS = 10                         # number of virtual users
    SPAWN_RATE = 2                         # users spawned per second
    RUN_TIME = "30s"                       # total duration of the test

    subprocess.run([
        "locust",
        "-f", __file__,
        "--headless",
        "--host", TARGET_HOST,
        "-u", str(NUM_USERS),
        "-r", str(SPAWN_RATE),
        "--run-time", RUN_TIME
    ])
