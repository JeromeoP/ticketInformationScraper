import requests
from bs4 import BeautifulSoup
import time
import threading
from plyer import notification
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_website(url):
    logging.info("Fetching the website...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching the website: {e}")
        return None

def parse_articles(html):
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('a', href=True)
    logging.info(f"Found {len(articles)} articles.")
    return articles

def check_for_biljettinfo():
    url = "https://www.arsenal.se/"
    html = fetch_website(url)
    if html is None:
        return

    articles = parse_articles(html)
    found = False
    for article in articles:
        if "Biljettinfo:" in article.text:
            logging.info(f"Found matching article: {article.text}")
            notify_user(f"Ny biljettinfo: {article.text}")
            found = True
            break

    if not found:
        notify_user("Ingen ny biljettinformation funnen")

def notify_user(message):
    def send_notification():
        notification.notify(
            title="Biljettinfo Notification",
            message=message,
            timeout=10
        )
        logging.info(f"Notification sent: {message}")

    thread = threading.Thread(target=send_notification)
    thread.start()

if __name__ == "__main__":
    check_for_biljettinfo()
