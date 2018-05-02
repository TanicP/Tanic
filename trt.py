import requests, json
has_more = True
page = 1
lines = 0
while (lines <= 50 and has_more):
    url = 'https://api.stackexchange.com/2.2/questions?pagesize=20&order=desc&sort=activity&tagged=python&site=stackoverflow'
    payload = {'page': page}
    result =requests.get(url, params=payload)
    if result.status_code == 200:
        for key in result.json().get('items'):
            if lines <= 50:
                print(key['title'])
            lines = lines + 1
    has_more = result.json().get('has_more')               
    page = page + 1