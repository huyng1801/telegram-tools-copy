import requests
import json

url = "http://localhost:3001/api/auth/login"

payload = json.dumps({
  "email": "admin@example.com",
  "password": "admin123456"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
