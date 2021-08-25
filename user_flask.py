import requests

print(requests.get('http://127.0.0.1:4444/?name=Yehuda').text)
print(requests.get('http://127.0.0.1:4444/exp?num1=2').text)