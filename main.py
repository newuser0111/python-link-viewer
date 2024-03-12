import schedule
import time
import webbrowser

# Function to open the link
def open_link():
    link = "https://pixeldrain.com/u/H3pgFS48"
    webbrowser.open(link)

# Schedule the job to run every 3.5 months (approximately)
schedule.every(105 * 24 * 60 * 60).seconds.do(open_link)

# Main loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
