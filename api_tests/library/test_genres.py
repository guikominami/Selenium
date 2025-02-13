import requests


def list_genres():

    url = "https://library-07f2.onrender.com/api/genres"
    response = requests.get(url)

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


if __name__ == "__main__":

    list_genres()
