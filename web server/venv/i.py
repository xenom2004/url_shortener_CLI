import requests
import json
r=requests.get(r"https://ab21.pythonanywhere.com/dd")
p=(r.text)
print(type(p))
# new_dictionary=json.loads((r))