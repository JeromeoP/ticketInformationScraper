import requests
from bs4 import BeautifulSoup
import time
import threading
from plyer import notification

def check_for_biljettinfo():
    url = "https://www.arsenal.se/"
    print("Fetching the website...")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', href=True)
    print(f"Found {len(articles)} articles")

    found = False
    for article in articles:
        if "Biljettinfo:" in article.text:
            notify_user(f"New Biljettinfo article: {article.text}")
            found = True
            break

    if not found:
        notify_user("Inga information om matchbiljetter finns tillgänglig.")

def notify_user(message):
    def send_notification():
        notification.notify(
            title="Biljettinfo Notification",
            message=message,
            timeout=10
        )
        print(f"Notification sent: {message}")

    thread = threading.Thread(target=send_notification)
    thread.start()

if __name__ == "__main__":
    check_for_biljettinfo()
