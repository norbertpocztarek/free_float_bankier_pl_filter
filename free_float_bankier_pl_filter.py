# -*- coding: utf-8 -*-
import requests
import re
import csv
import pandas as pd
from datetime import datetime

r = requests.get('https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ARTERIA')
company_names = requests.get('https://www.bankier.pl/gielda/notowania/akcje')
company_names.encoding = company_names.apparent_encoding  # it's overriding encoding to UTF-8 to see polish letters
company_names2 = company_names.text
# company_temp = company_names2.find('<a title=')
# print(company_temp)
# free_float = r.text
# x = free_float
# new = free_float.find("Free float")

print()
print()
# print("Free float for ARTERIA is: " + x[new+19:new+25])
print("")
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

c = 4  # columns
r = len(company_names_list)  # rows
companies_data_array = [[0] * c for i in range(r)]  # with each element value as 0
for i in range(r):
    for j in range(c):
        one_line = company_names_list[i]
        if j == 0:
            short_name_search = one_line.find(">")
            last_sign = len(one_line)
            short_company_name = one_line[short_name_search + 1: last_sign - 4]
            companies_data_array[i][j] = short_company_name
        if j == 1:
            long_name_search_first = one_line.find("=")
            long_name_search_last = one_line.find(" href")
            long_company_name = one_line[long_name_search_first + 2: long_name_search_last - 1]
            companies_data_array[i][j] = long_company_name
        if j == 2:
            http_address_search_first = one_line.find("href=")
            http_address_search_last = one_line.find('">')
            http_address = "https://www.bankier.pl" + one_line[http_address_search_first + 6: http_address_search_last]
            companies_data_array[i][j] = http_address


r = len(companies_data_array)  # rows
for i in range(r):
    # http_site_address = companies_data_array[i][2]
    free_float_get = requests.get(companies_data_array[i][2])
    free_float_get.encoding = free_float_get.apparent_encoding  # it's overriding encoding to UTF-8 to see polish letters
    free_float = free_float_get.text
    new = free_float.find("Free float")
    companies_data_array[i][3] = free_float[new + 19:new + 24]
    print(str(i)+"/"+str(r))


# print(companies_data_array)

now = datetime.now() # current date and time
date_time = now.strftime("%Y-%m-%d")
df = pd.DataFrame(companies_data_array)
df.columns =['Short', 'Full', 'HTTP', 'Free float [%]']
df.to_csv(date_time + ' GPW stocks.csv', encoding='utf-8-sig')

