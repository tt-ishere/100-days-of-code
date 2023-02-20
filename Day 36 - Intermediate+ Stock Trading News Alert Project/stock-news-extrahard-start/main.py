import requests
import datetime
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "K1BLUVDZ755LHSWQ"
NEWS_API_KEY = "5529be8532f448c091902fc3cd3465eb"
stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"
account_sid = "AC32bfbbb6f5c1a52b3e4b2e422e6092a1"
auth_token = "a034f796bf57d81e218a02c2f3013d3a"
stock_param = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_param = {
    "q": COMPANY_NAME,
    "searchIn": {"title", "description"},
    "sortBy": "popularity",
    "language": "en",
    "apikey": NEWS_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_response = requests.get(stock_url, stock_param)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# yesterdays price
yesteday_data = data_list[0]
yesterday_closing_price = float(yesteday_data["4. close"])

# day before yesterday price
day_before_yesteday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesteday_data["4. close"])

# calculate the percentage of increase/decrease
price_difference = yesterday_closing_price - day_before_yesterday_closing_price

diff_percentage = round((price_difference / yesterday_closing_price) * 100)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if diff_percentage > 1:
    news_response = requests.get(news_url, news_param)
    three_articles = news_response.json()["articles"][:3]
    formatted_article = [
        f"Headline: {article['title']} \nBrief: {article['description']}\n"
        for article in three_articles
    ]

    if price_difference > 0:
        stock_direction = f"🔼 {diff_percentage}%"
    else:
        stock_direction = f"🔽 {diff_percentage}%"

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    for news_item in formatted_article:
        msg_body = f"{STOCK}: {stock_direction}\n{news_item}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=msg_body,
            from_="+17407167716",
            to="+233268125555",
        )
        print(message.status)
