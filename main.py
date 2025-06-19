# Importing modules

from bs4 import BeautifulSoup
import requests
import time

news_data = []


def catch_error(news, var_tag, var_class):
    try:
        var = news.find(var_tag, class_=var_class).text
    except Exception as e:
        var = "N/A"
        # print(f"Error: {e}")
    return var




def get_news():
    html_text = requests.get("https://www.theguardian.com/international").text
    soup = BeautifulSoup(html_text, 'lxml')

    news_list = soup.find_all('div', class_='dcr-1555ajk')  # , id = "container-news")

    for news in news_list:
        headline = catch_error(news, 'span', 'show-underline dcr-uyefka')


        # category = news.find('div', class_="dcr-1cc5b8d").text
        category = catch_error(news, 'div', 'dcr-1cc5b8d')

        summary = catch_error(news, 'div', 'dcr-11jmxnw')

        publish_time = catch_error(news, 'footer', 'dcr-vfsw4m')

        more_info = news.find('a')['href']
        if "https://www.theguardian.com" not in more_info:
            more_info = f"https://www.theguardian.com{more_info}"

        if headline != 'N/A':
            if summary != 'N/A':
                if publish_time != 'N/A':
                    print(f"Headline: {headline}\nCategory: {category}\nSummary: {summary}\nPublish Time: {publish_time}\nMore Info: {more_info}\n\n")



def main():
    get_news()


if __name__ == '__main__':
    main()

