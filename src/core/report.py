import json
import os
from datetime import datetime

from config.settings import (
    LEETCODE_USERNAME,
    CODECHEF_USERNAME,
    GFG_USERNAME,
    HACKERRANK_USERNAME,
    CODE360_USERNAME,
    CODOLIO_USERNAME
)


class ReportGenerator:

    def load_json(self, path):

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)

        return None

    # -------------------------------------------------

    def generate_header(self):

        report = "# 🚀 CodePortfolioSync Dashboard\n\n"

        report += "## 👤 Developer\n\n"
        report += "**Name:** Beesu Naga Durga Neelasa\n\n"
        report += f"**Last Updated:** {datetime.now().strftime('%d-%m-%Y %H:%M')}\n\n"
        report += "---\n\n"

        return report

    # -------------------------------------------------

    def generate_summary(self):

        report = "## 📊 Platform Summary\n\n"

        report += "| Platform | Status |\n"
        report += "|----------|--------|\n"
        report += "| 🟠 LeetCode | ✅ |\n"
        report += "| 🟤 CodeChef | ✅ |\n"
        report += "| 🟢 GeeksforGeeks | ✅ |\n"
        report += "| 🔵 HackerRank | ✅ |\n"
        report += "| 🟣 Code360 | ✅ |\n"
        report += "| 🟡 Codolio | ✅ |\n\n"

        report += "---\n\n"

        return report

    # -------------------------------------------------

    def generate_leetcode(self):

        report = ""

        data = self.load_json("reports/leetcode.json")

        if data:

            stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

            report += "## 🟠 LeetCode\n\n"
            report += f"✔ **Total Solved:** {stats[0]['count']}\n\n"
            report += f"🟢 Easy : {stats[1]['count']}\n\n"
            report += f"🟡 Medium : {stats[2]['count']}\n\n"
            report += f"🔴 Hard : {stats[3]['count']}\n\n"
            report += f"🔗 https://leetcode.com/u/{LEETCODE_USERNAME}/\n\n"
            report += "---\n\n"

        return report

    # -------------------------------------------------

    def generate_codechef(self):

        report = ""

        data = self.load_json("reports/codechef.json")

        if data:

            report += "## 🟤 CodeChef\n\n"
            report += f"👤 Username : {data.get('username', 'N/A')}\n\n"
            report += f"⭐ Rating : {data.get('rating', 'N/A')}\n\n"
            report += f"🏆 Highest Rating : {data.get('highest_rating', 'N/A')}\n\n"
            report += f"🌍 Global Rank : {data.get('global_rank', 'N/A')}\n\n"
            report += f"🇮🇳 Country Rank : {data.get('country_rank', 'N/A')}\n\n"
            report += f"🔗 https://www.codechef.com/users/{CODECHEF_USERNAME}\n\n"
            report += "---\n\n"

        return report

    # -------------------------------------------------

    def generate_simple_platform(self, title, emoji, filename, username, profile_url):

        report = ""

        data = self.load_json(filename)

        if data:

            report += f"## {emoji} {title}\n\n"
            report += f"👤 Username : {username}\n\n"
            report += f"✅ Status : {data.get('status', 'Connected')}\n\n"
            report += f"🔗 {profile_url}\n\n"
            report += "---\n\n"

        return report

    # -------------------------------------------------

    def generate_footer(self):

        report = "## 🤖 Generated Automatically\n\n"
        report += "**CodePortfolioSync**\n\n"
        report += "Made with ❤️ using Python\n"

        return report

    # -------------------------------------------------

    def generate(self):

        report = ""

        report += self.generate_header()
        report += self.generate_summary()
        report += self.generate_leetcode()
        report += self.generate_codechef()

        report += self.generate_simple_platform(
            "GeeksforGeeks",
            "🟢",
            "reports/gfg.json",
            GFG_USERNAME,
            f"https://www.geeksforgeeks.org/profile/{GFG_USERNAME}"
        )

        report += self.generate_simple_platform(
            "HackerRank",
            "🔵",
            "reports/hackerrank.json",
            HACKERRANK_USERNAME,
            f"https://www.hackerrank.com/profile/{HACKERRANK_USERNAME}"
        )

        report += self.generate_simple_platform(
            "Code360",
            "🟣",
            "reports/code360.json",
            CODE360_USERNAME,
            f"https://www.naukri.com/code360/profile/{CODE360_USERNAME}"
        )

        report += self.generate_simple_platform(
            "Codolio",
            "🟡",
            "reports/codolio.json",
            CODOLIO_USERNAME,
            f"https://codolio.com/profile/{CODOLIO_USERNAME}"
        )

        report += self.generate_footer()

        # Save report in reports folder
        with open("reports/daily_report.md", "w", encoding="utf-8") as file:
            file.write(report)

        # Update GitHub README
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(report)

        print("Daily report generated successfully.")
        print("README.md updated successfully.")