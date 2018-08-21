'''
First time interacting with the REST API. Just trying to learn the ropes here.
Using the Guild Wars 2 API v2 available at:

    https://api.guildwars2.com/v2/

First part is requesting the daily achievements and referencing them with the
fully directory of gw2 achievements to identify the current dailies.

'''
import requests

BASE_URL = 'https://api.guildwars2.com/v2/'

resp = requests.get(BASE_URL + 'achievements/daily')

#if the status code is something besides 200, something is wrong
if resp.status_code != 200:
    #This means something went wrong, give the error code
    print(resp.status_code)

dailyIds = []
for todo_item in resp.json():
    for item in resp.json()[todo_item]:
        dailyIds.append(item['id'])
    
    '''
    for item in todo_item:
        print(item)
        #print('{} {}'.format(item['id'], item['level']))
    '''
print(dailyIds)

achievementResp = requests.get(BASE_URL + 'achievements')
for daily in dailyIds:
    achievementResp = requests.get(BASE_URL + 'achievements/' + str(daily))
    print(achievementResp.json()['name'])

