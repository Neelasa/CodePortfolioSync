"""
Synchronization Module
"""

class PortfolioSync:

    def __init__(self):
        self.platforms = [
            "CodeChef",
            "LeetCode",
            "GeeksforGeeks",
            "HackerRank",
            "Code360",
            "Codolio"
        ]

    def sync(self):
        print("Starting synchronization...")
        for platform in self.platforms:
            print(f"Checking {platform}...")
        print("Synchronization completed.")

if __name__ == "__main__":
    PortfolioSync().sync()
