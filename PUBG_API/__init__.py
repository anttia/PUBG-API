import requests
import os

def pubg_api_request(api_url):
    api_key = os.environ['PUBG_API_KEY']
    resp = requests.get(api_url, headers={
        'Authorization': 'Bearer ' + api_key,
        'Accept': 'application/vnd.api+json'
    })
    return resp.json()

def pubg_api_get_player_data(account_id):
    return pubg_api_request("https://api.pubg.com/shards/pc-eu/players/%s" % account_id)

def pubg_api_match_data(match_id):
    return pubg_api_request("https://api.pubg.com/shards/pc-eu/matches/%s" % match_id)

