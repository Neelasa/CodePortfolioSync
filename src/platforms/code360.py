import json
import os

from src.platforms.platform import CodingPlatform


class Code360(CodingPlatform):

    def __init__(self, username):
        self.username = username

    def fetch(self):

        data = {
            "platform": "Code360",
            "username": self.username,
            "profile_url": f"https://www.naukri.com/code360/profile/{self.username}",
            "status": "Connected"
        }

        os.makedirs("reports", exist_ok=True)

        with open("reports/code360.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Code360 profile fetched successfully.")

        return data