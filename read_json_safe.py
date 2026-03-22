import requests

CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"

r = requests.get("https://httpbin.org/json", timeout=10, verify=CA_BUNDLE)
r.raise_for_status()

data = r.json()

slideshow = data.get("slideshow", {})
title = slideshow.get("title")
slides = slideshow.get("slides", [])
missing_value = data.get("missing_key", "not_found")

print("title:", title)
print("slides_count:", len(slides))
print("missing_value:", missing_value)
