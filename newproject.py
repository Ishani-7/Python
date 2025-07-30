import requests
token="8035367427:AAFQgicxKsnu2SIfridprf3_j721wfSHa14"
chat_id = "@nepnewsreader"
url = f'https://api.telegram.org/bot{token}/sendMessage'
news_url = "https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts?limit=9"
r =requests.get(url=news_url)
data = r.json()['data']['news']
for i in data:
 
    title = i['title']
    link = i['link']
    message = f'''
<b>{title}!</b>  For more: <a href="{link}">Click Here</a>.
'''
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode":"HTML"
    }
    r = requests.post(url=url, data=params)
    print(r.text)
    break
    print(title, link)