import json
import requests

response = requests.get("https://api.github.com/search/users?q=forkim")
# q in the users?q=... is the query parameter
 
json_data = response.json()

print(json_data['total_count'])
 
print(json_data['items'][1]['html_url'])


 
