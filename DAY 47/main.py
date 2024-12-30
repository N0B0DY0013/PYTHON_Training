import os
import dotenv
import requests
import smtplib
from bs4 import BeautifulSoup

AMAZON_PRODUCT_ = "https://www.amazon.com/Dell-Precision-5490-Mobile-Workstation/dp/B0D4QSZLW2/ref=sr_1_3?crid=1KSOG7I8H130K&dib=eyJ2IjoiMSJ9.UFGT7MhEeyD4KzDuzeXubJMRcssMpyQ1dLamQ38exRrToJ4X_YTUjMMEf9LC24DmOuNQHFLkCPFtXn25VxHjKiAOqvuxCTa2RBTkuX__LacyIPyfbaAQaM8hgOJa_UgtB5knDs3mThumY4rvOth33yKOvlF2kLq3RU_6CgyFTzOg8yOyya62BnH4N_EmbDQTjQ_9BRaA_KPqFx71i4cbYk5NVMAz7dzIVMYczzst8IA.XcPAA73lcWQtgMt1H01kdCqAkaXZyQ4Cr5kjEypqXXU&dib_tag=se&keywords=dell+precision+5490&qid=1735546367&sprefix=dell+precision+54%2Caps%2C440&sr=8-3"

dotenv.load_dotenv()

sender_email = os.getenv("GOOGLE_SENDER_EMAIL")
sender_app_password = os.getenv("GOOGLE_SENDER_APP_PASSWORD")

response = requests.get(AMAZON_PRODUCT_, headers = {"User-Agent": "Mozilla/5.0",
                                                    "Accept-Language" : "en-US"})
response.raise_for_status()

price_page = BeautifulSoup(response.text, "html.parser").select_one(selector = "#corePriceDisplay_desktop_feature_div")
price_page = price_page.getText().strip().split("    ")[0]
price = float(price_page.replace(",", "").replace("$", ""))

if price > 2000:
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        
        connection.login(user = sender_email, password = sender_app_password)
        connection.sendmail(from_addr = sender_email,
                            to_addrs = "achameburti@gmail.com",
                            msg = f"This product is something you wanted to buy because the price is now {price_page}.\n\n{AMAZON_PRODUCT_}")

print("Done!")