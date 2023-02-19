import requests
import json
import time
def hasher(a):
    two_place=int((a-a%(100*52))/(100*52))
    b=int(a-two_place*(100*52))
    one_place=int((b-b%(100))/100)
    b=b-one_place*(100)
    zero_place=b
    li='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return f'{li[two_place]}{li[one_place]}{zero_place}'

    




long_url=input("Enter your url to be shortened..")
r=requests.get(r"https://ab21.pythonanywhere.com/dd")
new_dictionary=json.loads(r.text)
val=False
for x in new_dictionary:
    if(x==long_url):
        new_url=new_dictionary[x]
        val=True
if(val==False):
    code=hasher(len(new_dictionary))
    new_url=f'ab21.pythonanywhere.com/{code}'
    new_input={long_url:new_url}
    new_input=json.dumps(new_input)
    head={"Content-Type":"application/json"}
    response=requests.post(r"http://ab21.pythonanywhere.com/ll",data=new_input,headers=head)
print("Your new shortened url is :: " + new_url) 
time.sleep(15)       









