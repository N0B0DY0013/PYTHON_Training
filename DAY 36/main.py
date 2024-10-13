import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime,timedelta

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()

ALPHA_VANTAGE_CO_API_KEY = os.getenv("ALPHA_VANTAGE_CO_API_KEY")
NEWS_API_ORG_API_KEY = os.getenv("NEWS_API_ORG_API_KEY")

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_REG_NUMBER = os.getenv("TWILIO_REG_NUMBER")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


response_stock = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_VANTAGE_CO_API_KEY}")
response_stock.raise_for_status()

data = {}
data = response_stock.json()

curr_date_minus_one = (datetime.today() - timedelta(days = 2)).strftime("%Y-%m-%d")
curr_date_minus_two = (datetime.today() - timedelta(days = 3)).strftime("%Y-%m-%d")

curr_date_minus_one_data = data["Time Series (Daily)"][curr_date_minus_one]
curr_date_minus_two_data = data["Time Series (Daily)"][curr_date_minus_two]

delta_percent = (abs(float(curr_date_minus_two_data["4. close"]) - float(curr_date_minus_one_data["4. close"])) / float(curr_date_minus_one_data["4. close"]))

print(delta_percent)

if delta_percent >= 0.05:
    print("GET NEWS...")
    
    response_news = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME.lower()}&apiKey={NEWS_API_ORG_API_KEY}&to={datetime.today().strftime('%Y-%m-%d')}")
    response_news.raise_for_status()
    
    data = {}
    data = response_news.json()
    
    articles = data["articles"][:3]
    
    news = f"{STOCK}: {'🔺' if float(curr_date_minus_two_data['4. close']) < float(curr_date_minus_one_data['4. close']) else '🔻'} {round(delta_percent, 3)}%\n\n\n"
    
    for article in articles:
        news = news + f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
    
    print(news)
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(body = news,
                                     from_ = TWILIO_NUMBER,
                                     to = TWILIO_REG_NUMBER)
    
    