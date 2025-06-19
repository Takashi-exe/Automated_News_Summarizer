# Importing modules
from bs4 import BeautifulSoup
import requests
from utils import catch_get_data_error, url

# Store News data into a string
news_data = []

# This function retrieves News articles from the website
def get_news():
    # Html generated from the website
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    # List of all the available articles
    news_list = soup.find_all('div', class_='dcr-1555ajk')  # , id = "container-news")

    for news in news_list:
        # Article meta data
        title = catch_get_data_error(news, 'span', 'show-underline dcr-uyefka')
        category = catch_get_data_error(news, 'div', 'dcr-1cc5b8d')
        summary = catch_get_data_error(news, 'div', 'dcr-11jmxnw')
        publish_time = catch_get_data_error(news, 'footer', 'dcr-vfsw4m')

        # Link for more information on given articles
        more_info = news.find('a')['href']
        # Some links may not be complete, the if statement below checks and completes them
        if "https://www.theguardian.com" not in more_info:
            more_info = f"https://www.theguardian.com{more_info}"

        # The following conditions filter out articles with incomplete data
        if title != 'N/A':
            if summary != 'N/A':
                if publish_time != 'N/A':
                    print(f"Headline: {title}\nCategory: {category}\nSummary: {summary}\nPublish Time: {publish_time}\nMore Info: {more_info}\n\n")



def main():
    get_news()


if __name__ == '__main__':
    main()

