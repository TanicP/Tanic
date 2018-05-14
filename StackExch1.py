import requests, json
import pandas as pd
def buildUrl(page, pagesize, tagged):
    return 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&page={0}&pagesize={1}&tagged={2}'.format(page, pagesize, tagged)

pagesize = 20
tagged = 'python'
linesQuan = 50
has_more = True
page = 1
lines = 0

frame = pd.DataFrame()
ser = pd.Series()

while (lines <= linesQuan and has_more):
    result = requests.get(buildUrl(page, pagesize, tagged))
    if result.status_code != 200:
         break
    else :     
        for key in result.json().get('items'):
            if lines < linesQuan:
                frame = frame.append(pd.Series([key['title']]), ignore_index=True)
            lines = lines + 1
        has_more = result.json().get('has_more')               
        page = page + 1
     
        
frame.head(linesQuan)       