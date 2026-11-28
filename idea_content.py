#!/usr/bin/env python3

from gemini import idea_from_gemini
from gsheet import get_all_records, get_last_record, append_records
from utils import log_progress

def brainstorm():
	log_progress("Brainstorm started!")
	last_record = get_last_record()
	if last_record is None:
		last_number = 0
	else:
		last_number = last_record["no"]

	log_progress("Request idea to gemini")
	prompt = f"You are the script-writing idea content psychology for a channel that turns questions people think are simple, obvious, or already-settled into videos that make viewers stop scrolling, watch to the end, and argue in the comments. You give me 30 ideas content psycology with with format table no, topic. Starting with number > {last_number}"

	data = idea_from_gemini(prompt)

	log_progress("Append idea to gsheet")
	success = append_records(data)

	if success:
		log_progress("Append success")
	else:
		log_progress("Append failed")

	log_progress("Brainstorm completed!")

brainstorm()
