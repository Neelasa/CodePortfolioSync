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

        print(response.json())
