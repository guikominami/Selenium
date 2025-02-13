import requests
from register_user import autenticate_user
from test_data import users_auth_admin, genre


def list_genres(token):

    header = headers = {"User-Agent": "my-app/0.0.1"}
    url = "https://library-07f2.onrender.com/api/genres"
    response = requests.get(url, headers=header)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("GET request successful!")
        print("Response:")
        print()

        data_genres_json = response.json()
        print(type(data_genres_json))

        for genre in data_genres_json:
            print(f'Id: {genre["_id"]} - name: {genre["name"]}')

    else:
        print(f"GET request failed with status code {response.status_code}")


def create_genre(token):

    header = {"x-auth-token": token}
    url = "https://library-07f2.onrender.com/api/genres"
    response = requests.post(url, json=genre, headers=header)

    if response.status_code == 200:
        print("POST request successful!")
        print()

        print("Response:")
        print(f"body: {response.content}")
        print()
    else:
        print(
            f"POST request failed with status code {response.status_code} - ERROR: {response.content}"
        )


if __name__ == "__main__":

    token = autenticate_user(users_auth_admin)
    create_genre(token)
