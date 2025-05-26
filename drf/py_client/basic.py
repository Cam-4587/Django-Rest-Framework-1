import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world"})
# print(get_response.text)
print(get_response.json())
# get_response = requests.get(endpoint, params={"abc": 123},  json={"query": "Hello World"})

# print(get_response.text)
# print(get_response.status_code)

# print(get_response.json()['message'])

# # Define the endpoint for a 200 status code
# endpoint = "http://httpbin.org/status/200"  # This URL returns a 200 status code

# # Make the GET request
# get_response = requests.get(endpoint)

# # print the response content
# print(f"Response Content: {get_response}")

# # Print the HTTP status code
# print(f"Status Code: {get_response.status_code}")


# # Define the endpoint for a website
# endpoint = "https://httpbin.org"
# # Make the GET request
# get_response = requests.get(endpoint)

# # print the response contnet
# print(f"Response Content (to get status code): {get_response}")

# # print the response content in text form
# print("Response Content in Text Form (prints out the HTML content of the webpage):")
# print(get_response.text)



# # Define endpoint for another website
# endpoint = "https://httpbin.org/anything"

# # Make the GET request
# get_response = requests.get(endpoint)

# # print the response contnet
# print(f"Response Content (to get status code): {get_response}")

# # print the response content in JSON form
# print("Response Content in JSON Form (prints out the json data from the website):")
# print(get_response.json())




# # Define endpoint for another website
# endpoint = "https://httpbin.org/anything"

# # Alter the GET request to add hello world in the in the json data as form data
# get_response = requests.get(endpoint, data={"query": "Hello World"})

# # print the response content in JSON form
# print("Response Content in JSON Form (prints out the json data from the website with the addition of hello world):")
# print(get_response.json())


# # Define endpoint for another website
# endpoint = "https://httpbin.org/anything"

# # Alter the GET request to add hello world in the in the json data
# get_response = requests.get(endpoint, json={"query": "Hello World"})

# # print the response content in JSON form
# print("Response Content in JSON Form (prints out the json data from the website with the addition of hello world):")
# print(get_response.json())

