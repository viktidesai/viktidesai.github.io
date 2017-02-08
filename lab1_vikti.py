# importing libraries

import Twitter
import json 
import OAuth
import TwitterHTTPError
import TwitterStream

#setting acess tokens and keys variables. 
ACCESS_TOKEN = '1452186060-iTnEjhru2Pu1j2QEKBG7KfM3fiAmjGF1hBEOrv4'
ACCESS_SECRET = 'lzJPDGoIG4upbR2JuO6d2947JiheCTbIjMEZ5VqYnyEGZ'
consumer_key= 'X5RhO7yFb6Q5cGH88jiQyHydo'
consumer_secret = '41fzBrObmaFnueUHlFN3cC6fKx5g830A0ZB1vflxxBTGWWeJgA' 
oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET, consumer_key, consumer_secret)
twitter = Twitter(auth = oauth)
twitter.search.tweets(q='#trump')
twitter.search.tweets(q='#trump', result_type='recent', lang='en', count=10)
world_trends = twitter.trends.available(_woedid=1)

# finding trends for various cities.
sa_trends = twitter.trends.place(_id = 56120136)
sfo_trends = twitter.trends.place(_id = 2487956)
chic_trends = twitter.trends.place(_id = 2379574)
dallas_trends = twitter.trends.place(_id =2388929)
newyork_trends = twitter.trends.place(_id =2459115)
wash_trends=twitter.trends.place(_id=2347606)
phil_trends=twitter.trends.place(_id=2471217)

# printing out results
print(json.dumps(sa_trends, indent=4))
print(json.dumps(sfo_trends, indent=4))
print(json.dumps(chic_trends, indent=4))
print(json.dumps(dallas_trends, indent=4))
print(json.dumps(newyork_trends, indent=4))
print(json.dumps(wash_trends, indent=4))
print(json.dumps(phil_trends, indent=4))





