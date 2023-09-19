import requests
#import the library requests

r = requests.get('putwebsiteURlhere')

web_headers = r.headers
print("Here are the returned headers")
print(web_headers)

web_html = r.text
print("here is the returned html of the body")
print(web_html)

web_status_code = r.status_code
print("here is the returned HTTP status code")
print(web_status_code)

web_cookies = r.cookies
print("here are the returned cookies")
print(web_cookies)
