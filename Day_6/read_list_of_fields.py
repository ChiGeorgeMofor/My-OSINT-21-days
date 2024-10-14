import json
import requests

response = requests.get("https://api.github.com/search/users?q=folefac")

json_data = response.json()

usersCount = len(json_data['items'])-1

for x in range(usersCount):
    print(json_data['items'][x]['html_url'])

# Also we can use slice.. To fetch the first ten user objects
# for user in json_data['items'][:10]:
#    print(user['html_url'])
