import requests
import json
from test_data import users
from test_data import users_auth_admin, users_auth_no_admin


def create_user():

    url = "https://library-07f2.onrender.com/api/users"

    for user in users:
        print(user)

        response = requests.post(url, json=user)

        if response.status_code == 200:
            print("POST request successful!")
            print()

            print("Response:")
            print(f"body: {response.content}")
            print()

            token = response.headers["x-auth-token"]
            print(f"header: {token}")

        else:
            print(
                f"POST request failed with status code {response.status_code} - ERROR: {response.content}"
            )


def autenticate_user(user):

    url = "https://library-07f2.onrender.com/api/auth"

    response = requests.post(url, json=user)

    if response.status_code == 200:
        print("POST request successful!")
        print()

        token = response.text
        print("Response:")
        print(token)
        print()

        return token

    else:
        print(
            f"POST request failed with status code {response.status_code} - ERROR: {response.content}"
        )


if __name__ == "__main__":

    # create_user()

    token = autenticate_user(users_auth_admin)
    print(token)

    token = autenticate_user(users_auth_no_admin)
    print(token)
