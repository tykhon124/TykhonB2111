import requests

res_parse_list = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
res_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startwith('$')
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswich("$") and parse_elem_1