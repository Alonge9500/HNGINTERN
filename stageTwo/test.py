import requests
import json


BASE_URL = "http://localhost:5000"

def print_response(response):
    try:
        response_json = response.json()
        print(json.dumps(response_json, indent=4))
    except json.JSONDecodeError:
        print(response.text)

# Test POST endpoint
def test_create_person():
    data = {
        "name": "John",
        "age": 30,
        "gender": "Male"
    }
    response = requests.post(f"{BASE_URL}/person", json=data)
    print("POST /person:")
    print_response(response)

# Test PUT endpoint
def test_update_person():
    data = {
        "age": 35,
        "gender": "Male"
    }
    response = requests.put(f"{BASE_URL}/person/John", json=data)
    print("PUT /person/John:")
    print_response(response)

# Test GET endpoint
def test_get_person():
    response = requests.get(f"{BASE_URL}/person/John")
    print("GET /person/John:")
    print_response(response)

# Test DELETE endpoint
def test_delete_person():
    response = requests.delete(f"{BASE_URL}/person/John")
    print("DELETE /person/John:")
    print_response(response)

if __name__ == "__main__":
    test_create_person()
    test_update_person()
    test_get_person()
    test_delete_person()
