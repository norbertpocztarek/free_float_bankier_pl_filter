import requests

r = requests.get('https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ARTERIA')
free_float = r.text
x = free_float
new = free_float.find("Free float")
print()
print()
print("Free float for ARTERIA is: " + x[new+19:new+25])
print()
#print(r.text)