import requests
CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"
def main() -> None:
    try:
        r = requests.get("https://example.com", timeout=10, verify=CA_BUNDLE)
        r.raise_for_status()
        print("status:", r.status_code)
        print("first_80_chars:", r.text[:80].replace("\n", " "))
    except requests.exceptions.RequestException as e:
        print("request_failed:", type(e).__name__)
        print("details:", e)
if __name__ == "__main__":
    main()
