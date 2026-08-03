from src.leetcode import LeetCode
from src.report import ReportGenerator
from config.settings import LEETCODE_USERNAME


def main():

    print("=" * 60)
    print("🚀 CodePortfolioSync")
    print("=" * 60)

    lc = LeetCode(LEETCODE_USERNAME)
    lc.fetch()

    report = ReportGenerator()
    report.generate()

    print("\nFramework executed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()