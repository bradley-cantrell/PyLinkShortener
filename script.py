#Take long link
#Check for valid link
#Shorten link by hashing the original link and building a url like www.fake-shorten.com/hash
#Store the long_link, short_link, hash, and a chronological link_id in a hashmap 


long_urls = input("Enter a comma separated list of long URLs:\n").split(",")

def shortenurl(long_urls):
    urldict = []
    
    for n, url in enumerate(long_urls):
        hashed_url = hash(url)
        short_url = "www.shorten-url.com/" + str(hashed_url)
        
        urldict.append({
            'long_url': url,
            'short_url': short_url,
            'id': n
        })
    
    print(urldict)
shortenurl(long_urls)