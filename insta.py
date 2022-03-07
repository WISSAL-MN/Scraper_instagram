from instascrape import *
# import requests
# from bs4 import BeautifulSoup
# url="https://www.instagram.com/accounts/onetap/?next=%2F&hl=fr"
# response = request.get(url)
# soup = BeautifulSoup(response.text)
# script = soup.findAll('script',{'type ':'text/javascript'})[3].text
# print (script)
# Instantiate the scraper objects 
google = Profile('https://www.instagram.com/accounts/onetap/?next=%2F&hl=fr')
google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
google_hashtag = Hashtag('https://www.instagram.com/explore/tags/google/')

# Scrape their respective data 
google.scrape()
google_post.scrape()
google_hashtag.scrape()

print(google.followers)
print(google_post['hashtags'])
print(google_hashtag.amount_of_posts)