import requests

url = "http://127.0.0.1:8000/agent-assist/"

query = input("Please enter your query: ")

payload = {"query": query}

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("\nResponse:", response.json()["response"])
    else:
        print("Failed to get a response from the server. Status code:", response.status_code)
except Exception as e:
    print("Error:", e)
