# -*- coding: utf-8 -*-
import requests
import re

r = requests.get('https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ARTERIA')
company_names = requests.get('https://www.bankier.pl/gielda/notowania/akcje')
company_names2 = company_names.text
# company_temp = company_names2.find('<a title=')
# print(company_temp)
free_float = r.text
x = free_float
new = free_float.find("Free float")
# new2 = free_float.find("script")
# new3 = free_float.find("script")

# print(new2)
# print(new3)
print()
print()
print("Free float for ARTERIA is: " + x[new+19:new+25])
print()
result = ([m.start() for m in re.finditer('<a title=', company_names2)])
# print(result)

# text = company_names2
# left_text = company_names2.split("</a>")[20]
split_text = company_names2.splitlines()
# result2 = ([m.start() for m in re.finditer('<a title=', split_text)])
# print(left_text)
# print(result2)
# print(r.text)
r = re.compile(".*<a title=")
company_names_list = list(filter(r.match, split_text)) # Read Note below
first_line = company_names_list[145]

short_name_search = first_line.find(">")
last_sign = len(first_line)
short_company_name = first_line[short_name_search+1: last_sign-4]

long_name_search_first = first_line.find("=")
long_name_search_last = first_line.find(" href")
long_company_name = first_line[long_name_search_first+2: long_name_search_last-1]

http_address_search_first = first_line.find("href=")
http_address_search_last = first_line.find('">')
http_address = "https://www.bankier.pl" + first_line[http_address_search_first+6: http_address_search_last]

# list_of_companies

c = 3  # columns
r = len(company_names_list)  # rows
companies_data_array = [[0] * c for i in range(r)]  # with each element value as 0
print(company_names_list)