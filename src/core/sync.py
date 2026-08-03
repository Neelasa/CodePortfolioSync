"""
Synchronization Module

Coordinates data collection from all supported coding platforms.
"""

from src.platforms.leetcode import LeetCode
from src.platforms.codechef import CodeChef

from config.settings import (
    LEETCODE_USERNAME,
    CODECHEF_USERNAME
)


class PortfolioSync:

    def __init__(self):

        self.platforms = [
            LeetCode(LEETCODE_USERNAME),
            CodeChef(CODECHEF_USERNAME)
        ]

    def run(self):

        print("=" * 60)
        print("Starting CodePortfolioSync...")
        print("=" * 60)

        results = []

        for platform in self.platforms:

            try:

                data = platform.fetch()

                if data:
                    results.append(data)

            except Exception as error:

                print(f"Error while syncing {platform.__class__.__name__}")
                print(error)

        print("\nSynchronization completed successfully.")

        return results


if __name__ == "__main__":

    sync = PortfolioSync()
    sync.run()