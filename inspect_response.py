import requests
CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"
r = requests.get("https://example.com", timeout=10, verify=CA_BUNDLE)
print("type:", type(r).__name__)
print("satus_code:", r.status_code)
print("content_type:", r.headers.get("Content-type"))
print("text_len:", len(r.text))
print("first_60:", r.text[:60].replace("\n", " "))
