import json
import os
import requests
from bs4 import BeautifulSoup

from src.platforms.platform import CodingPlatform


class GeeksForGeeks(CodingPlatform):

    def __init__(self, username):
        self.username = username

    def fetch(self):

        profile_url = f"https://www.geeksforgeeks.org/profile/{self.username}"
        leaderboard_url = "https://practice.geeksforgeeks.org/leaderboard"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        data = {
            "platform": "GeeksforGeeks",
            "username": self.username,
            "name": "",
            "rank": "",
            "score": "",
            "profile_url": profile_url
        }

        # -----------------------------
        # Fetch Name from Profile Page
        # -----------------------------
        try:
            response = requests.get(profile_url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                h1 = soup.find("h1")

                if h1:
                    data["name"] = h1.get_text(strip=True)

        except Exception:
            pass

        # -----------------------------
        # Fetch Rank & Score
        # -----------------------------
        try:
            response = requests.get(leaderboard_url, headers=headers, timeout=10)

            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                rows = soup.find_all("tr")

                for row in rows:

                    text = row.get_text(" ", strip=True)

                    if self.username in text:

                        values = row.find_all("td")

                        if len(values) >= 3:
                            data["rank"] = values[1].get_text(strip=True)
                            data["score"] = values[2].get_text(strip=True)

                        break

        except Exception:
            pass

        os.makedirs("reports", exist_ok=True)

        with open("reports/gfg.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("GeeksforGeeks profile fetched successfully.")

        return data