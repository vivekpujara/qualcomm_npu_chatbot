import requests
import yaml
from prettyprinter import pprint

def workspaces(
    api_key = 'ZSX04G3-9H34XW5-JB631QJ-NQBN2Q0',
    base_url = 'http://localhost:3001/api/v1'
) -> None:
    """
    prints unformatted json info about the available workspaces. Used
    to identify the correct workspace slug for the chat api call
    """
    workspaces_url = base_url + "/workspaces"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    workspaces_response = requests.get(
        workspaces_url,
        headers=headers
    )

    if workspaces_response.status_code == 200:
        print("Successful authentication")
    else:
        print("Authentication failed")

    pprint(workspaces_response.json())

if __name__ == "__main__":
    # load config from yaml
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    api_key = config["api_key"]
    base_url = config["model_server_base_url"]

    workspaces(api_key, base_url)