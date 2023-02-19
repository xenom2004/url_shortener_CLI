import requests
import json
d={"e":1}
D=json.dumps(d)
header={"Content-Type":"application/json"}

response=requests.post(r"https://ab21.pythonanywhere.com/ll",headers=header,data =D)
print(response)