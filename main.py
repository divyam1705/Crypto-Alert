STOCK = "ADA"
COMPANY_NAME = "Cardano"
import requests
from twilio.rest import Client
api_key_alpha=""
api_key_news=""
params={"function":"CRYPTO_INTRADAY","market":"INR","symbol":"ADA","apikey":api_key_alpha,"interval":"60min"}
response=requests.get("https://www.alphavantage.co/query",params=params)
response.raise_for_status()
data=response.json()
print(data)
perdeviation=((yest-daybyest)/daybyest)*100
perdeviation=round(perdeviation,2)

# STEP 1: Use https://www.alphavantage.co
#When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
#Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

headline=""
desc=""
def getnews():
    global headline,desc
    parameter = {"q": COMPANY_NAME, "apiKey": api_key_news}
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameter)
    data1 = response.json()
    headline=data1["articles"][0]["title"]
    desc=data1["articles"][0]["description"]


account_sid=""
auth_token=""
decsym=""
if perdeviation >5:
    sym=f"🔺{perdeviation}%"
elif perdeviation<-5:
    sym=f"🔻{perdeviation}%"
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if perdeviation >5 or perdeviation<-5:
    getnews()

    msg=f"{COMPANY_NAME}:{sym}\nHeadline:{headline}\nBrief:{desc}"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,
        from_='whatsapp:'  ,
        to='whatsapp:+'
        )
    print(message.status)