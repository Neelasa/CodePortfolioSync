import json
import os
import requests


class LeetCode:

    def __init__(self, username):
        self.username = username

    def fetch(self):

        url = "https://leetcode.com/graphql"

        query = """
        query getUserProfile($username: String!) {
          matchedUser(username: $username) {
            username
            submitStats {
              acSubmissionNum {
                difficulty
                count
              }
            }
          }
        }
        """

        response = requests.post(
            url,
            json={
                "query": query,
                "variables": {
                    "username": self.username
                }
            }
        )

        data = response.json()

        os.makedirs("reports", exist_ok=True)

        with open("reports/leetcode.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return data