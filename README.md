# 42_api_requests

Boiler plate code in python to authenticate the 42 API and get a token to request public information

The print_logtime function is used to get logtime data from a specific time period and then piped with 'wc -l' to get logtime days + 2 

.env file structure :

```API_USER="Base64 encoded"
API_URL=""
API_UID=""
API_SECRET=""
START_TIME="YYYY-MM-DD"
END_TIME="YYYY-MM-DD"
