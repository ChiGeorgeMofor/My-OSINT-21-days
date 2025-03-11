def capitalizeAllWords(x):
    return x.title()

cities = ['new york', 'dublin', 'london']

result = map(capitalizeAllWords, cities)

print(list(result))