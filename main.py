"""
CodePortfolioSync
Developer Portfolio Automation Framework

Author: Beesu Naga Durga Neelasa
"""

import datetime
from src.sync import PortfolioSync


def main():
    print("=" * 60)
    print("🚀 CodePortfolioSync")
    print("=" * 60)
    print("Status              : Active")
    print("Framework           : Initialized")
    print("GitHub Actions      : Connected")
    print("Supported Platforms :")
    print("   • CodeChef")
    print("   • LeetCode")
    print("   • GeeksforGeeks")
    print("   • HackerRank")
    print("   • Code360")
    print("   • Codolio")
    print("Started At          :", datetime.datetime.now())
    print("=" * 60)

    print("\nStarting synchronization...\n")

    sync = PortfolioSync()
    sync.sync()

    print("\nSynchronization completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
