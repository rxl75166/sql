import sys
import os
import requests

def check_sql_injection(url):
  # Inject a SQL statement into the headers
  headers = { "OR": "1=1" }

  # Send a request with the injected headers
  response = requests.get(url, headers=headers)

  # If the response is different from the normal response, it is vulnerable to SQL injection
  if response != requests.get(url):
    return True
  else:
    return False

# Check if the argument is a file or a single URL
if os.path.isfile(sys.argv[1]):
  # Read the list of URLs from the file
  with open(sys.argv[1], "r") as f:
    url_list = f.read().splitlines()

  # Test each URL for SQL injection vulnerabilities
  for url in url_list:
    if check_sql_injection(url):
      print(f"{url} is vulnerable to SQL injection!")
    else:
      print(f"{url} is not vulnerable to SQL injection.")
else:
  # Test the single URL for SQL injection vulnerabilities
  if check_sql_injection(sys.argv[1]):
    print(f"{sys.argv[1]} is vulnerable to SQL injection!")
  else:
    print(f"{sys.argv[1]} is not vulnerable to SQL injection.")
