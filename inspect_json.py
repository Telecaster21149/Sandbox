import requests
CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"
html_resp = requests.get("https://example.com", timeout=10, verify=CA_BUNDLE)
print("html_content_type:", html_resp.headers.get("Content-Type"))
try:
    data = html_resp.json()
    print("html_json_ok:", data)
except Exception as e:
    print("html_json_failed:", type(e).__name__)
json_resp = requests.get("https://httpbin.org/json", timeout=10, verify=CA_BUNDLE)
json_resp.raise_for_status()
print("json_content_type:", json_resp.headers.get("Content-Type"))
print("json_top_type:", type(json_resp.json()).__name__)
print("json_keys:", list(json_resp.json().keys()))
