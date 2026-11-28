import gspread
import pandas as pd

from datetime import datetime
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

def get_last_record():
	df_records = get_all_records()

	if not df_records.empty:
		last_record = df_records.iloc[-1].to_dict()
	else:
		last_record = None
	return last_record

def get_all_records():
	sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1pvt-H43dprR4k53d2oI9kRYrqfYc9BnQSh6WEi1z0Zw/edit")
	worksheet = sheet.worksheet("Sheet1")

	df_records = pd.DataFrame(worksheet.get_all_records())
	return df_records

def append_records(items):
	sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1pvt-H43dprR4k53d2oI9kRYrqfYc9BnQSh6WEi1z0Zw/edit")
	worksheet = sheet.worksheet("Sheet1")

	headers = worksheet.row_values(1)
	rows_data = items_to_rows(items, headers)

	if rows_data:
		worksheet.append_rows(rows_data, value_input_option="USER_ENTERED")
		return True
	else:
		return False

def items_to_rows(items: list[dict], headers: list[str])-> list[list]:
	if not items or not headers:
		return []

	df = pd.DataFrame(items)
	now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	df["created_at"] = now_str

	return df[headers].values.tolist()
