import os
import requests
from cachetools import cached, TTLCache

@cached(cache=TTLCache(maxsize=20, ttl=10800))
def getWarStatistic():
    apiUrl = os.getenv("APIURL")
    
    response = requests.get(url=apiUrl)
    data = []
    
    for x in response.json():
        url = str(x['api_url'])
        url = url.replace("net//", "net/")
        url = url.replace("2022//", "2022/")
    
        response = requests.get(url=url)
        data.append(response)
        
    return data
    
    
        
    
    
    
