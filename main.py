import requests
CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"
r = requests.get("https://example.com", timeout=10, verify=CA_BUNDLE)
print("status:", r.status_code)
print("first_80_chars:", r.text[:80].replace("\n", " "))
