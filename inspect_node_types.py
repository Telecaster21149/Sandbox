import requests

CA_BUNDLE = "/etc/ssl/certs/ca-certificates.crt"

r = requests.get("https://httpbin.org/json", timeout=10, verify=CA_BUNDLE)
r.raise_for_status()

data = r.json()
slideshow = data.get("slideshow", {})
slides = slideshow.get("slides", [])
first_slide = slides[0] if slides else None

print("data_type:", type(data).__name__)
print("slideshow_type:", type(slideshow).__name__)
print("slides_type:", type(slides).__name__)
print("first_slide_type:", type(first_slide).__name__)

print("is_data_dict:", isinstance(data, dict))
print("is_slides_list:", isinstance(slides, list))
print("is_first_slide_dict:", isinstance(first_slide, dict))
