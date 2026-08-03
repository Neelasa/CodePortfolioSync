from src.core.sync import PortfolioSync
from src.core.report import ReportGenerator


def main():

    sync = PortfolioSync()

    sync.run()

    report = ReportGenerator()
    report.generate()

    print("\nFramework executed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()