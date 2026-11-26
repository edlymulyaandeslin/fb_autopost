#!/usr/bin/env python3

import requests

PAGE_ID = "102563849383447"
PAGE_ACCESS_TOKEN = "EAAiWbhrokQwBTAELpnmqsaRt7uU3FXIO5K3oJoxHKdPBvSu4J0PLloJmthhZAQhnpBZBncsKL8S77EMEckdKxHSsb7T0dW3CUXt35PCuzBdGPvWLVHnLbiyo60HAo9qVbn4XijuetVZC7IG6jvmrYb3FFaRZAylLwZCYOyCOyoHL73EbKjfZBXc6Fp0ZAfpPFJLcFoZD"


url = f"https://graph.facebook.com/v27.0/{PAGE_ID}/feed"

data = {
	"message": "Hello this is the automate posts",
	"access_token": PAGE_ACCESS_TOKEN
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.json())
