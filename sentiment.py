"""Run sentiment analysis on the text of each tweeet
   start packaging back the store with location, no text unfortunately
"""

KEY = '894fc27b-f874-48f0-a624-042ba2a63d1c'

from havenondemand.hodclient import *
import json
from get_tweets import getTweets

# to get to user tex, we do obj.text
tweets = getTweets()

client = HODClient(KEY, version="v1")

# take this out later
# testing by cutting tweets in half
print 'the numebr of tweets has been cut to ', len(tweets)

def getScores():
    scores = []

    for obj in tweets:

        params = {'text': obj.text}

        response_async = client.post_request(params, HODApps.ANALYZE_SENTIMENT, async=True)
        jobID = response_async['jobID']
        response = client.get_job_result(jobID)

        print response
        print '\n'

        # print response['aggregate']['score']
        score_value = response['aggregate']['score']
        sentiment = str(response['aggregate']['sentiment'])

        # push into the new dict
        final_dict = {}
        final_dict['positive'] = abs(score_value)
        final_dict['name'] = obj.user.location

        if sentiment == 'positive' or sentiment == 'neutral':
            final_dict['color'] = 'blue'
        else:
            final_dict['color'] = 'red'

        scores.append(final_dict) 

    return scores


print 'the final dict we gon use is \n'

scores = getScores()

for s in scores:
    print s

# another filter here to take average the opinions of the same state





