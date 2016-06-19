'''Use twitter api to search for tweets on a specify topic
   see if we can get location too
'''

import twitter

CONSUMER = 'zaVMgRSwOmxUSgLTR8E0FBol4'
CONSUMER_SECRET = 'UGLFQgodNseLRMyIbuj2oG8wJnaOxyqf7S3j4PFOdby1qr8619'
ACCESS = '744270321440677888-VTFsg9BpCrLCvTVOOP1G12Xbjx6af3S'
ACCESS_SECRET = 'RQzxgkoqxQJaqM8EGXCJgKmTeL1HhXTPiXhEoHE1IFoJn'

api = twitter.Api(consumer_key = CONSUMER,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS, 
                  access_token_secret = ACCESS_SECRET)

# the only thing needed from the tweets are the location and text
# text passes through sentiment analysis
# location needs to be fixed and there will be further filtering on that

def getTweets():

    results = api.GetSearch(raw_query="q=guncontrol%20&result_type=recent&since=2016&count=100")


    # get rid of location after
    location = []
    locationUsers = [] # this contains the tweets still

    for obj in results:
        user = obj.user

        try:
            if user.location:
                location.append(user.location)
                locationUsers.append(obj) #filter yo

        except AttributeError:
            pass

    return locationUsers

# print 'the total tweets that have location si ', len(location)
# print 'location \n'
# print location 
    

# ok, have the objets
# print 'the total tweets that have location si ', len(locationUsers)
# print 'tweets\n'
# print locationUsers
 
# expecting a function here to filter the bad locations, not in USA






# f = open('dummy.txt', 'w')
# f.write(str(location))
# f.close()







