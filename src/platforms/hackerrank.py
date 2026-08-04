import json
import os

from src.platforms.platform import CodingPlatform


class HackerRank(CodingPlatform):

    def __init__(self, username):
        self.username = username

    def fetch(self):

        data = {
            "platform": "HackerRank",
            "username": self.username,
            "profile_url": f"https://www.hackerrank.com/profile/{self.username}",
            "status": "Connected"
        }

        os.makedirs("reports", exist_ok=True)

        with open("reports/hackerrank.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("HackerRank profile fetched successfully.")

        return data