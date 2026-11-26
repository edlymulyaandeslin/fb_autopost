#!/usr/bin/env python3

import requests

USER_ACCESS_TOKEN = "EAAiWbhrokQwBTJpbfa53RCEBXh6hSkBHplec7ibCkn7ZBDtb9ojoiTZAFHHtteeibpO2vBd9RZCIrKUc9g1qaK0YxjH0C2NBQzoamMn8z1FRCMSZBFmeAPvV8K4D8qLPwE2coZASY9ha87IQ6S4UtBCpv2vUxX4p7wY5ZB4nrhIrKPxPT7NKuvbHaZCRZBymo55kgn2U5xDw65vDlolFlSAmeb42vuQVBzl2TGeDyGn81HXtINuFOQZDZD"

url = "https://graph.facebook.com/v27.0/me/accounts"

params = {
	"access_token": USER_ACCESS_TOKEN
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())
