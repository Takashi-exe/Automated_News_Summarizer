# configparser module lets us use urls from the config file
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
url = config['Settings']['url']

# Checks for errors while retrieving data from articles, returns "NA" if there isn't available data
def catch_get_data_error(news, var_tag, var_class):
    try:
        var = news.find(var_tag, class_=var_class).text
    except Exception as e:
        var = "N/A"
        # print(f"Error: {e}")
    return var


