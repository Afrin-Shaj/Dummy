import requests

url = "https://seven.snsihub.tech/generate"  # IMPORTANT: use HTTPS
headers = {
    "Content-Type": "application/json",
    "x-api-key": "testing"
}
payload = {
    "prompt": "What is full form of AWS?"
}

response = requests.post(url, json=payload, headers=headers, timeout=60)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)

print("Parsed Response:", response.json())  

payload = response.json()
