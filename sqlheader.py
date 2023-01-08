import sys
import os
import requests

def check_sql_injection(url, payload):
  # Inject the payload into the headers
  headers = { "OR": payload }

  # Send a request with the injected headers
  response = requests.get(url, headers=headers)

  # If the response is different from the normal response, it is potentially vulnerable to SQL injection
  if response != requests.get(url):
    # Try injecting a second payload to confirm the vulnerability
    headers = { "OR": payload + "--" }
    response = requests.get(url, headers=headers)
    if response != requests.get(url):
      return True
  return False

# Get the name of the file containing the list of payloads from the command-line arguments
payload_file = sys.argv[1]

# Read the list of payloads from the file
with open(payload_file, "r") as f:
  payload_list = f.read().splitlines()

# Check if the argument is a file or a single URL
if os.path.isfile(sys.argv[2]):
  # Read the list of URLs from the file
  with open(sys.argv[2], "r") as f:
    url_list = f.read().splitlines()

  # Test each URL for SQL injection vulnerabilities using each payload
  for url in url_list:
    for payload in payload_list:
      if check_sql_injection(url, payload):
        print(f"{url} is potentially vulnerable to SQL injection using payload {payload}!")
      else:
        print(f"{url} is not vulnerable to SQL injection using payload {payload}.")
else:
  #
