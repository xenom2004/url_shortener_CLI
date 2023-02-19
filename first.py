# import requests
   
# # Making a GET request
# r = requests.get('https://api.github.com/users/naveenkrnl')
  
# # check status code for response received
# # success code - 200
# # print(r)
# print(r.status_code)
  
# # print content of request
# # print(r.content)
import requests

# Making a POST request
r = requests.post('https://httpbin.org / post', data ={'key':'value'})

# check status code for response received
# success code - 200
print(r)

# print content of request
# print(r.json())
