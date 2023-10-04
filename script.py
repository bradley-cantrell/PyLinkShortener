#Take long link
#Check for valid link
#Shorten link by hashing the original link and building a url like www.fake-shorten.com/hash
#Store the long_link, short_link, hash, and a chronological link_id in a list 
import hashlib
import base64
import random
import string

long_urls = input("Enter a comma-separated list of long URLs:\n").split(",")

def shortenurl(long_urls):
    urldict = {}
    charset = string.ascii_letters + string.digits  # Alphanumeric characters
    short_url_length = 7
    
    for n, url in enumerate(long_urls):
        # Hash the long URL using SHA-256
        hashed_url = hashlib.sha256(url.encode()).digest()
        
        # Encode the hash in base64 and convert it to a string
        encoded_url_bytes = base64.urlsafe_b64encode(hashed_url)
        encoded_url = encoded_url_bytes.decode().rstrip("=")  # Remove padding characters
        
        # Ensure short URL uniqueness
        while True:
            unique_short_url = ''.join(random.choice(charset) for _ in range(short_url_length))
            if unique_short_url not in urldict:
                break
        
        # Create the short URL
        short_url = "www.fake-shorten.com/" + unique_short_url
        
        urldict[unique_short_url] = {
            'long_url': url,
            'id': n
        }
    
    for short_url, entry in urldict.items():
        print(f"Long URL: {entry['long_url']}")
        print(f"Short URL: ", f"https://www.fake-shorten.com/{short_url}")
        print(f"ID: {entry['id']}\n")

shortenurl(long_urls)
