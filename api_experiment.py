import requests

def get_random_joke(host, path="/", port=80):
    """
    TODO:

    1. Send a GET request to "https://api.chucknorris.io/jokes/random"
    2. Check response.status_code — if it's NOT 200, print an error
       message and return None
    3. If it IS 200, get the parsed JSON using .json()
    4. Pull out just the joke text — you saw the key name when you
       printed the response earlier. Which field held the actual joke?
    5. Return that value
    """

    response = requests.get(f"https://{host}{path}")

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    else:
        joke_json = response.json()
        joke_text = joke_json.get("value")

    return joke_text

if __name__ == "__main__":
    joke = get_random_joke("api.chucknorris.io", "/jokes/random")
    print(joke)