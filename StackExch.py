import requests, json
import pandas as pd
url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'
pagesize = 20
tagged = 'python'
linesQuan = 50
has_more = True
page = 1
lines = 0
error = False
frame = pd.DataFrame()
ser = pd.Series()
while (lines <= linesQuan and has_more and not error):
    payload = {'page': page, 'pagesize': pagesize, 'tagged': tagged}
    result =requests.get(url, params=payload)
    if result.status_code == 200:
        for key in result.json().get('items'):
            if lines < linesQuan:
                frame = frame.append(pd.Series([key['title']]), ignore_index=True)
                print(key['title'])
            lines = lines + 1
        has_more = result.json().get('has_more')               
        page = page + 1
    else : 
        error = True
        break
print('end')        