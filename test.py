import requests

response = requests.get('https://api.coinstats.app/public/v1/coins?skip=0&limit=10&currency=USD')
print(response.json()['coins'])