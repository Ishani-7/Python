#requests
#http request

#pip install requests

#get and post

import requests

url='https://api.restful-api.dev/objects'
r=requests.get(url=url)
if r.status_code==200:
    data=r.json()
    for i in data:
        # print(i)
         print(f'Name: {i['name']}')

url="https://www.onlinekhabar.com/smtm/home/advance-decline/nepse"
r=requests.get(url=url)
if r.status_code==200:
    data=r.json()
    final_data=data['response']
    for i in final_data:
        print(f'''
transactions :{i['transactions']},
total share traded:{i['shares_traded']}
'''
        )

url="https://www.onlinekhabar.com/smtm/home/market-calendar"
r=requests.get(url=url)
if r.status_code==200:
    data=r.json()
    final_data=data['response']
    for i in final_data:
        print(f'''
            date:{i["date"]},
            company_name:{i['company_name']},
            allotment:{i['allotment']}
''')
 
#202,204,201
#400-499 (user end error)
#500-599 (server error)

