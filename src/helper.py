import requests
from src.constants import API_KEY, BASE_URL, BASE_URL_V5

headers = {"X-Riot-Token": API_KEY}


def get_request(path: str):
    return requests.get(BASE_URL + path, headers=headers)


def get_request_v5(path: str, params={}):
    return requests.get(BASE_URL_V5 + path, headers=headers)
