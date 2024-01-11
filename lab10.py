# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS

# Add some comments of what these request are doing to your script

from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:")

# Prompt the user to type a string input as the variable for your destination URL.
url = "https://github.com/CoreyGray45/SaavyCoders"
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
print(f"Request to be sent: {b} {url}")
confirmation = input("Please confirm to proceed. (y/n): ")

if confirmation.lower() == "y":
    # Using the requests library, perform a GET request to your github.
    response = requests.request(b, "https://github.com/CoreyGray45/SaavyCoders")

    # For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

    status_code = response.status_code
    if status_code == 200:
        status = "OK"
    elif status_code == 201:
        status = "Created"
    elif status_code == 204:
        status = "No Content"
    elif status_code == 400:
        status = "Bad Request"
    elif status_code == 401:
        status = "Unauthorized"
    elif status_code == 403:
        status = "Forbidden"
    elif status_code == 404:
        status = "Not Found"
    elif status_code == 500:
        status = "Internal Server Error"
    else:
        status = "Unknown"

    print(f"Status: {status}")
   
else:
    print("Input Error.")