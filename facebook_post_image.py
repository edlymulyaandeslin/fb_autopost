#!/usr/bin/env python3

import requests

PAGE_ID = "102563849383447"
PAGE_ACCESS_TOKEN = "EAAiWbhrokQwBTAELpnmqsaRt7uU3FXIO5K3oJoxHKdPBvSu4J0PLloJmthhZAQhnpBZBncsKL8S77EMEckdKxHSsb7T0dW3CUXt35PCuzBdGPvWLVHnLbiyo60HAo9qVbn4XijuetVZC7IG6jvmrYb3FFaRZAylLwZCYOyCOyoHL73EbKjfZBXc6Fp0ZAfpPFJLcFoZD"

url = f"https://graph.facebook.com/v27.0/{PAGE_ID}/photos"

FILE_ID = "171w-W7VJ3eQ16wwWvYe15OnHNOzA8yPr"  # Ambil ID dari URL Google Drive[span_4](start_span)[span_4](end_span)
direct_url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

data = {
	"url": direct_url,
	"message": "Its me!",
	"access_token": PAGE_ACCESS_TOKEN
}

response = requests.post(url, data=data)

if response.status_code == 200:
	print("Posting berhasil!")
	print(response.json())
else:
	print("Posting failed!")
	print(response.status_code)
	print(response.text)
