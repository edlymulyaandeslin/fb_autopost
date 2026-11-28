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

def idea_from_gemini(prompt):
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

	return data

