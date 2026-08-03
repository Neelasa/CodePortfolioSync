import json
import os
from datetime import datetime


class ReportGenerator:

    def generate(self):

        file_path = "reports/leetcode.json"

        if not os.path.exists(file_path):
            print("No report found.")
            return

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

        username = data["data"]["matchedUser"]["username"]

        total = stats[0]["count"]
        easy = stats[1]["count"]
        medium = stats[2]["count"]
        hard = stats[3]["count"]

        today = datetime.now().strftime("%d-%m-%Y %H:%M")

        report = f"""# CodePortfolioSync

## Developer

{username}

Generated On: {today}

---

## LeetCode Statistics

Total Solved : {total}

Easy : {easy}

Medium : {medium}

Hard : {hard}

---

Generated Automatically by CodePortfolioSync
"""

        with open("reports/daily_report.md", "w", encoding="utf-8") as file:
            file.write(report)

        print("Daily report generated successfully.")