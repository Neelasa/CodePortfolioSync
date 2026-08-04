import json
import os

from src.platforms.platform import CodingPlatform


class Codolio(CodingPlatform):

    def __init__(self, username):
        self.username = username

    def fetch(self):

        data = {
            "platform": "Codolio",
            "username": self.username,
            "profile_url": f"https://codolio.com/profile/{self.username}",
            "status": "Connected"
        }

        os.makedirs("reports", exist_ok=True)

        with open("reports/codolio.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Codolio profile fetched successfully.")

        return data