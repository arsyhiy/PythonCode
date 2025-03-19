import requests

# Making a GET request
r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

# check status code fore response received
# succes code -- 200
print(r)


# print content of request
print(r.content)
