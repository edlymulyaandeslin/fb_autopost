#!/usr/bin/env python3

import requests, os
import argparse

from dotenv import load_dotenv
from utils import log_progress

load_dotenv()

parser = argparse.ArgumentParser(
	description="Facebook post automation\nMade by Lin.",
	formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument("-t", "--type", required=True, help="Type post formatter: (text/image)")

args = parser.parse_args()

PAGE_ID = os.getenv("PAGE_ID")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

def post_text(PAGE_ID, PAGE_ACCESS_TOKEN, message):
	try:
		url = f"https://graph.facebook.com/v27.0/{PAGE_ID}/feed"

		data = {
			"message": message,
			"access_token": PAGE_ACCESS_TOKEN
		}

		response = requests.post(url, data=data)

		log_progress("Posting successfully!")
	except Exception as e:
		log_progress(f"Posting failed. ERROR: {e}")

def post_image(PAGE_ID, PAGE_ACCESS_TOKEN, message):
	try:
		url = f"https://graph.facebook.com/v27.0/{PAGE_ID}/photos"

		FILE_ID = "171w-W7VJ3eQ16wwWvYe15OnHNOzA8yPr"  # Ambil ID dari URL Google Drive[span_4](start_span)[span_4](end_span)
		direct_url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

		data = {
        		"url": direct_url,
		        "message": message,
        		"access_token": PAGE_ACCESS_TOKEN
		}

		response = requests.post(url, data=data)

		log_progress("Posting image successfully!")
	except Exception as e:
        	log_progress(f"Posting failed. ERROR: {e}")

type = args.type.lower()

if type == "text":
	log_progress("Post text starting...")
	post_text(PAGE_ID, PAGE_ACCESS_TOKEN, "Hi, good evening!")

elif type == "image":
	log_progress("Post image starting...")
else:
	log_progress("Invalid type formatter (text/image)")
