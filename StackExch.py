import requests, json
import pandas as pd
from pandas.io.json import json_normalize
def buildUrl(page, pagesize, tagged):
    return 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&page={0}&pagesize={1}&tagged={2}'.format(page, pagesize, tagged)

pagesize = 20
tagged = 'python'
linesQuan = 20
has_more = True
page = 1
lines = 0

while (lines <= linesQuan and has_more):
    result = requests.get(buildUrl(page, pagesize, tagged))
    if result.status_code != 200:
         break
    else :  
        if lines < linesQuan:
            df = pd.DataFrame.from_dict(json_normalize(result.json().get('items')), orient='columns')
        lines = lines + 1
    has_more = result.json().get('has_more')               
    page = page + 1     

df.head()    