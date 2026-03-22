import requests
CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"
r = requests.get("https://httpbin.org/json", timeout=10, verify=CA_BUNDLE)
r.raise_for_status()
data = r.json()
slideshow = data.get("slideshow", {})
slides = slideshow.get("slides", [])
print("slides_count:", len(slides))
for i, slide in enumerate(slides, start=1):
    title = slide.get("title", "untitled")
    slide_type = slide.get("type", "unknown")
    print(f"slide_{i}: title={title!r}, type={slide_type!r}")
