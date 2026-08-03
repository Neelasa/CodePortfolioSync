import json
import os
from datetime import datetime


class ReportGenerator:

    def generate(self):

        report = "# 🚀 CodePortfolioSync Dashboard\n\n"

        report += f"**Generated On:** {datetime.now().strftime('%d-%m-%Y %H:%M')}\n\n"

        report += "---\n\n"

        # =======================
        # LeetCode
        # =======================

        if os.path.exists("reports/leetcode.json"):

            with open("reports/leetcode.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

            report += "## 🟠 LeetCode\n\n"

            report += f"- Total Solved : {stats[0]['count']}\n"
            report += f"- Easy : {stats[1]['count']}\n"
            report += f"- Medium : {stats[2]['count']}\n"
            report += f"- Hard : {stats[3]['count']}\n\n"

        # =======================
        # CodeChef
        # =======================

        if os.path.exists("reports/codechef.json"):

            with open("reports/codechef.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            report += "## 🟤 CodeChef\n\n"

            report += f"- Username : {data.get('username', 'N/A')}\n"
            report += f"- Name : {data.get('name', 'N/A')}\n"
            report += f"- Country : {data.get('country', 'N/A')}\n"
            report += f"- Rating : {data.get('rating', 'N/A')}\n"
            report += f"- Division : {data.get('division', 'N/A')}\n"
            report += f"- Highest Rating : {data.get('highest_rating', 'N/A')}\n"
            report += f"- Global Rank : {data.get('global_rank', 'N/A')}\n"
            report += f"- Country Rank : {data.get('country_rank', 'N/A')}\n\n"

        report += "---\n\n"

        report += "Generated automatically by **CodePortfolioSync**."

        with open("reports/daily_report.md", "w", encoding="utf-8") as file:
            file.write(report)

        print("Daily report generated successfully.")