import requests
from test_data import users


def create_user():

    url = "https://library-07f2.onrender.com/api/users"

    response = requests.post(url, json=users)

    if response.status_code == 200:
        print("POST request successful!")
        print("Response:")
        print()
        print(response.text)

    else:
        print(
            f"POST request failed with status code {response.status_code} - error {response}"
        )


if __name__ == "__main__":

    create_user()
