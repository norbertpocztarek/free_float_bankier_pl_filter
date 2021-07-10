import requests

r = requests.get('https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ARTERIA')

print(r.text)
