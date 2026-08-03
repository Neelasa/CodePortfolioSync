from src.leetcode import LeetCode
from config.settings import LEETCODE_USERNAME


def main():

    lc = LeetCode(LEETCODE_USERNAME)

    lc.fetch()


if __name__ == "__main__":
    main()
