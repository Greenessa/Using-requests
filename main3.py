import requests
import pprint
url = "https://api.stackexchange.com/questions"
params = {"site": "stackoverflow", "fromdate": "1690588800", "todate": "1690675200", "tagged": "python"}
resp = requests.get(url, params=params).json()
#pprint.pprint(resp)
for i, question in enumerate(resp['items'], start = 1):
    print(f'{i}. {question["title"] }.')