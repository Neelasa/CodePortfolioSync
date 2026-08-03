import json
import os
import re

import requests
from bs4 import BeautifulSoup

from src.platforms.platform import CodingPlatform


class CodeChef(CodingPlatform):

    def __init__(self, username):
        self.username = username

    def fetch(self):

        url = f"https://www.codechef.com/users/{self.username}"

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        data = {
            "platform": "CodeChef",
            "username": self.username,
            "name": "",
            "country": "",
            "rating": "",
            "division": "",
            "highest_rating": "",
            "global_rank": "",
            "country_rank": ""
        }

        # Name
        h1 = soup.find("h1")
        if h1:
            data["name"] = h1.text.strip()

        text = soup.get_text(" ", strip=True)

        # Country
        country_match = re.search(r"Country:\s*([A-Za-z ]+)", text)
        if country_match:
            data["country"] = country_match.group(1).strip()

        # Rating
        rating_match = re.search(r"(\d+)\s*\(Div", text)
        if rating_match:
            data["rating"] = rating_match.group(1)

        # Division
        division_match = re.search(r"\((Div\s*\d+)\)", text)
        if division_match:
            data["division"] = division_match.group(1)

        # Highest Rating
        highest_match = re.search(r"Highest Rating\s*(\d+)", text)
        if highest_match:
            data["highest_rating"] = highest_match.group(1)

        # Global Rank
        global_match = re.search(r"(\d+)\s*Global Rank", text)
        if global_match:
            data["global_rank"] = global_match.group(1)

        # Country Rank
        country_rank_match = re.search(r"(\d+)\s*Country Rank", text)
        if country_rank_match:
            data["country_rank"] = country_rank_match.group(1)

        os.makedirs("reports", exist_ok=True)

        with open("reports/codechef.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("CodeChef profile fetched successfully.")

        return data