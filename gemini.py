from google import genai
from dotenv import load_dotenv
from google.genai import types
from pydantic import BaseModel

import os, json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class IdeaSchema(BaseModel):
	no: int
	topic: str

def req_to_gemini(prompt):
	client = genai.Client(api_key=GEMINI_API_KEY)

	response = client.models.generate_content(
		model="gemini-3.6-flash",
		contents=prompt,
		config=types.GenerateContentConfig(
			response_mime_type="application/json",
			response_schema=list[IdeaSchema]
		)
	)

	data = json.loads(response.text)
	print(data)
	return data

prompt = "You are the script-writing idea content psychology for a channel that turns questions people think are simple, obvious, or already-settled into videos that make viewers stop scrolling, watch to the end, and argue in the comments. You give me 30 ideas content psycology with with format table no, topic. and at the last response you confirm to me if i want 10 more content just wring more"

req_to_gemini(prompt)
