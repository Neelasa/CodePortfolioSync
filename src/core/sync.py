"""
Synchronization Module

Coordinates data collection from all supported coding platforms.
"""

from src.platforms.leetcode import LeetCode
from src.platforms.codechef import CodeChef
from src.platforms.gfg import GeeksForGeeks
from src.platforms.hackerrank import HackerRank
from src.platforms.code360 import Code360
from src.platforms.codolio import Codolio

from config.settings import (
    LEETCODE_USERNAME,
    CODECHEF_USERNAME,
    GFG_USERNAME,
    HACKERRANK_USERNAME,
    CODE360_USERNAME,
    CODOLIO_USERNAME
)


class PortfolioSync:

    def __init__(self):

        self.platforms = [
            LeetCode(LEETCODE_USERNAME),
            CodeChef(CODECHEF_USERNAME),
            GeeksForGeeks(GFG_USERNAME),
            HackerRank(HACKERRANK_USERNAME),
            Code360(CODE360_USERNAME),
            Codolio(CODOLIO_USERNAME)
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