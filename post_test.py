import requests
req = requests.post("http://localhost:8090/events2017/auth", data = {"name":"andrew","password":"letmein"})
print(req.text)
req.close()