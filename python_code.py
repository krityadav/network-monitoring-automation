import requests
device = "http://10.1.1.1/api/status"
response = requests.get(device)
if response.status_code == 200:
   print("Device healthy")
else:
   print("Device unreachable")
