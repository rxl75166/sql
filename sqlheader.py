import requests
import urllib


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

# Example usage
if check_sql_injection("http://example.com/search"):
  print("Vulnerable to SQL injection!")
else:
  print("Not vulnerable to SQL injection.")
