"""
CodePortfolioSync
Developer Portfolio Automation Framework

Author: Beesu Naga Durga Neelasa
"""

from src.sync import PortfolioSync
import datetime


def main():
    print("=" * 60)
    print("🚀 CodePortfolioSync")
    print("=" * 60)
    print(f"Started : {datetime.datetime.now()}")
    print()

    PortfolioSync().sync()

    print("\nFramework execution completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
