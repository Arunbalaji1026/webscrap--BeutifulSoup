import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Sony-BDV-E3200-Digital-Blu-ray-Theatre/dp/B00KBRXCDY/ref=sr_1_4?dchild=1&fst=as%3Aoff&pf_rd_i=1389387031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=7f489dbb-de4d-42a4-b529-b08d65b07314&pf_rd_r=3CWFJVJ14JGSJ1YVRVKD&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1562138511&refinements=p_72%3A1318477031%2Cp_85%3A10440599031%2Cp_89%3ASony&rnid=3837712031&rps=1&s=electronics&sr=1-4'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
     # print(soup.prettify()
     # IT will run the whole link we have applied
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id='priceblock_ourprice').get_text()[2:8]
    price = price.replace(',','')
    actual_price = float(price)
    while(actual_price < 26000):
        send_mail()

    print(title.strip())
    print(actual_price)



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('xyz@gmail.com', 'yrwhrozhxseoriye')
    # sevrer.login('hostmail', 'two way aunthentication code')

    subject= 'price has fell down !!'
    body = 'check the amazon link https://www.amazon.in/Sony-BDV-E3200-Digital-Blu-ray-Theatre/dp/B00KBRXCDY/ref=sr_1_4?dchild=1&fst=as%3Aoff&pf_rd_i=1389387031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=7f489dbb-de4d-42a4-b529-b08d65b07314&pf_rd_r=3CWFJVJ14JGSJ1YVRVKD&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1562138511&refinements=p_72%3A1318477031%2Cp_85%3A10440599031%2Cp_89%3ASony&rnid=3837712031&rps=1&s=electronics&sr=1-4'

    msg= f"Subject:{subject}\n\n{body}"

    server.sendmail(
        # From , the host
        # To the host back or to a friends mail !
        'xyz@gmail.com',
        'abc@gmail.com',
        msg
    )
    print('hey , email has been sent')

    server.quit()

check_price()
