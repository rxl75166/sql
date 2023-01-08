import sys
import os
import requests

def check_sql_injection(url, payloads):
  # Test each payload
  for payload in payloads:
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

# Read the list of payloads from a file
with open(sys.argv[1], "r") as f:
  payloads = f.read().splitlines()

# Check if the second argument is a file or a single URL
if os.path.isfile(sys.argv[2]):
  # Read the list of URLs from the file
  with open(sys.argv[2], "r") as f:
    url_list = f.read().splitlines()

  # Test each URL for SQL injection vulnerabilities
  for url in url_list:
    if check_sql_injection(url, payloads):
      print(f"{url} is potentially vulnerable to SQL injection!")
    else:
      print(f"{url} is not vulnerable to SQL injection.")
else:
  # Test the single URL for SQL injection vulnerabilities
  if check_sql_injection(sys.argv[2], payloads):
    print(f"{sys.argv[2]} is potentially vulnerable to SQL injection!")
  else:
    print(f"{sys.argv[2]} is not vulnerable to SQL injection.")
