import requests
import re

def find_subdomains(domain):
    subdomains = set()
    # Regular expression for matching subdomains
    pattern = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+' + domain
    # Get the contents of the parent domain's website
    try:
        parent_domain = requests.get('http://' + domain)
    except:
        parent_domain = requests.get('https://' + domain)
    # Search the contents for subdomains
    matches = re.finditer(pattern, parent_domain.text)
    for match in matches:
        subdomains.add(match.group())
    return subdomains

domain = input("Enter a domain: ")
subdomains = find_subdomains(domain)
print("Found subdomains:", subdomains)
