from os import getenv
from dotenv import load_dotenv
import base64
import requests
from datetime import datetime
import json
import logging
import binascii

logger = logging.basicConfig(level="INFO")
logger = logging.getLogger("api_logger")


def print_logtime(api_url: str, user_login: str, start_time: datetime, end_time: datetime, token: str):
	params = {
		"begin_at": start_time,
		"end_at": end_time
	}
	headers = {
		"Authorization": f"Bearer {token}"
	}
	res = requests.get(api_url + f"/v2/users/{user_login}/locations_stats", headers=headers, params=params)
	if res.status_code != 200:
		raise requests.HTTPError(f"API Logtime error: {res.status_code}")
	json_data = json.dumps(res.json(), indent=2)
	print(json_data)


def authenticate(api_url: str, api_uid: str, api_secret: str):
	params = {
		"grant_type": "client_credentials",
		"client_id": api_uid,
		"client_secret": api_secret
	}
	res = requests.post(api_url + "/oauth/token", params=params)
	if res.status_code != 200:
		raise requests.HTTPError(f"API Authentication error: {res.status_code}")
	res = res.json()
	return res.get("access_token")


if __name__ == "__main__":
	load_dotenv()
	try:
		api_user = base64.b64decode(getenv("API_USER")).decode('utf-8')
	except binascii.Error as err:
		logger.error(err)
		exit(1)
	api_url = getenv("API_URL")
	api_uid = getenv("API_UID")
	api_secret = getenv("API_SECRET")
	try:
		token = authenticate(api_url, api_uid, api_secret)
		print_logtime(api_url=api_url, user_login=api_user, start_time=getenv("START_TIME"), end_time=getenv("END_TIME"), token=token)
	except requests.HTTPError as err:
		logger.error(err)
