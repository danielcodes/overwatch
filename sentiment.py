from havenondemand.hodclient import *
import json
import tweepy
client = HODClient("894fc27b-f874-48f0-a624-042ba2a63d1c", version="v1")
# Get hashtags from twitter
params = {'text': 'I hate Haven OnDemand!'}
# Twitter Streaming API # Requires ESRI to handle dynamic data ..
#
# consumer_key=" "
# consumer_secret=" "
# access_token=" "
# access_token_secret=" "
response_async = client.post_request(params, HODApps.ANALYZE_SENTIMENT, async=True)
jobID = response_async['jobID']
response = client.get_job_result(jobID)
print response

# print response['aggregate']['score']
score_value=response['aggregate']['score']
print score_value
# Normalizing values in range bwetween 0 and 1
#   newvalue= (max'-min')/(max-min)*(value-max)+max'
score_value = score_value+1
print score_value










