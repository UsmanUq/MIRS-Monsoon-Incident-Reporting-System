import requests
try:
    response = requests.post("http://localhost:5000/report", 
                           json={"name": "test", "details": "something"})
    print(response.json())
except Exception as e:
    print(f"Error: {e}")
#this is a fast api test response query, keep for future testing for feature/exapnasion/migration