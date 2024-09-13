from pyshorteners import Shortener

ACCESS_TOKEN = "Get an Access token from bitly"

long_url = input()
url_shortener = Shortener(domain="bit.ly", api_key=ACCESS_TOKEN)
print("Short URL is : ", format(url_shortener.bitly.short(long_url)))
