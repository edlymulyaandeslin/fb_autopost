from datetime import datetime

def log_progress(message):
        timestamp = f"%Y-%m-%d %H:%M:%S"
        now = datetime.now()
        dateformat = now.strftime(timestamp)
        with open("./log.txt", "a") as file:
                file.write(f"{dateformat}: {message}\n")
        print(f"{dateformat}: {message}")
