import requests
CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt"
r = requests.get("https://httpbin.org/json", timeout=10, verify=CA_BUNDLE)
r.raise_for_status()
data = r.json()
print("top_type:", type(data).__name__)
print("top_keys:", list(data.keys()))
print("slideshow_type:", type(data["slideshow"]).__name__)
print("title:", data["slideshow"]["title"])
print("slides_type:", type(data["slideshow"]["slides"]).__name__)
print("slides_Count:", len(data["slideshow"]["slides"]))
