# from duckduckgo_search import ddg
import csv
 
csv_file = open('search_results.csv', 'w')
writer = csv.writer(csv_file, delimiter=';')

keywords = 'osint'
results = ddg(keywords, region='us-en', Safesearch='Off', time='y')

for x in range(len(results)):
    row = [results[x]['title'], results[x]['body'], results[x]['href']]
    writer = writer(row)

csv_file.close()
