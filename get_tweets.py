'''Use twitter api to search for tweets on a specify topic
   see if we can get location too
'''

States = {'AL':'alabama','AK':'alaska','AZ':'arizona','AR':'arkansa','CA':'california','CO':'colorado','CT':'connecticut','DE':'delaware','FL':'florida','GA':'georgia','HI':'hawaii','ID':'idaho','IL':'illinois','IN':'indiana','IA':'iowa','KS':'kansas','KY':'kentucky','LA':'louisiana','ME':'maine','MD':'maryland','MA':'massachusetts','MI':'michigan','MN':'minnesota','MS':'mississippi','MO':'missouri','MT':'montana','NE':'nebraska','NV':'nevada','NH':'new hampshire','NY':'new york','NC':'north carolina','ND':'north dakota','OH':'ohio','OK':'oklahoma','OR':'oregon','PA':'pennsylvania','RI':'rhode island','SC':'south carolina','SD':'south dakota','TN':'tenessee','TX':'texas','UT':'utah','VT':'vermont','VA':'virginia','WV':'west virginia','WI':'wisconsin','WY':'wyoming','GU':'guam','PR':'puerto rico','VI':'virgin islands', 'NJ': 'new jersey', 'WA': 'washington'}

# from twitter user.location, filter out non US places
# input is the array of tweets, looking for user.location
def getState(tweet):

    acro = States.keys()
    full = States.values()

#     print acro
#     print full

    # this needs verifying, location is a string
    location = tweet.user.location
    location = location.split(',') 

    # print location
    # for 'CA', ' USA', ' WA' cases, remove whitespace

    # if there are more than two items, check in
    # everything should fall under
    if len(location) == 2:
        # one item at a time
        # two if checks for each array
        location[1] = location[1].replace(' ', '')
        # print location

        if location[0] in acro:
            tweet.user.location = States[location[0]]
            return States[location[0]]

        if location[1] in acro:
            tweet.user.location = States[location[1]]
            return  States[location[1]]
    else: # one item

        if location[0] in acro:
            tweet.user.location = States[location[0]]
            return  States[location[0]]

    return None

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

    results = api.GetSearch(raw_query="q=guncontrol%20&result_type=recent&since=2015&count=100")

    # get rid of location after
    location = []
    locationUsers = [] # this contains the tweets still

    # after getting results, run the function to filter location

    for obj in results:
        user = obj.user

        try:
            if user.location and getState(obj):
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
