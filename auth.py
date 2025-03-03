import requests
import yaml

def auth(
    api_key = 'ZSX04G3-9H34XW5-JB631QJ-NQBN2Q0',
    base_url = 'http://localhost:3001/api/v1'
) -> None:
    """
    confirms the auth token is valid

    inputs:
        - api_key<string>: your api key
        - base_url<string>: the endpoint of the AnythingLLM local server
    """
    auth_url = base_url + "/auth"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + api_key
    }
    auth_response = requests.get(
        auth_url,
        headers=headers
    )

    if auth_response.status_code == 200:
        print("Successful authentication")
    else:
        print("Authentication failed")

    print(auth_response.json())

if __name__ == "__main__":
    # load config from yaml
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    api_key = config["api_key"]
    base_url = config["model_server_base_url"]

    auth(api_key, base_url)