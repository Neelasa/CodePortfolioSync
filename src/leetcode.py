import requests
import os

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

        variables = {
            "username": self.username
        }

        response = requests.post(
            url,
            json={
                "query": query,
                "variables": variables
            }
        )

        data = response.json()

        os.makedirs("reports", exist_ok=True)

        with open("reports/leetcode.json", "w") as file:
            import json
            json.dump(data, file, indent=4)

        print("LeetCode data saved successfully.")