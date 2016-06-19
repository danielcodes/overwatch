"""request to update all the states to a level ground of 0.4
   to send request, the object id of the state is needed, so created a dict with (state => id)

   to use: just import resetBlues and resetReds functions
"""

from sentiment import getScores
import requests

# dict (state => id)
state_ids = { 'hawaii': 1,
              'washington': 2,
              'montana': 3,
              'maine': 4,
              'north dakota': 5,
              'south dakota': 6,
              'wyoming': 7,
              'wisconsin': 8,
              'idaho': 9,
              'vermont': 10,
              'minnesota': 11,
              'oregon': 12,
              'new hampshire': 13,
              'iowa': 14,
              'massachusetts': 15,
              'nebraska': 16,
              'new york': 17,
              'pennsylvania': 18,
              'connecticut': 19,
              'rhode island': 20,
              'new jersey': 21,
              'indiana': 22,
              'nevada': 23,
              'utah': 24,
              'california': 25,
              'ohio': 26,
              'illinois': 27,
              'dc': 28,
              'delaware': 29,
              'west virginia': 30,
              'maryland': 31,
              'colorado': 32,
              'kentucky': 33,
              'kansas': 34,
              'virginia': 35,
              'missouri': 36,
              'arizona': 37,
              'oklahoma': 38,
              'north carolina': 39,
              'tennessee': 40,
              'texas': 41,
              'new mexico': 42,
              'alabama': 43,
              'mississippi': 44,
              'georgia': 45,
              'south carolina': 46, 
              'arkansas': 47,
              'louisiana': 48,
              'florida': 49,
              'michigan': 50,
              'alaska': 51,
            }


token = '9uoHmj0khoGE-IPi0suBX32onwoIAsSJzSZwpB1MKv8v5gwYkP382gLLNop5tA__HFQP-SX14R8h11vY6cXqKup_gH1zNs7CY4CIcK9wDCEJkejdMCtjNCfwAftlMpLqQOfEewk6nC_uMLOrWgUGJw..' 

url_blues = 'http://services3.arcgis.com/zBkEB8YtoDaCmWOf/arcgis/rest/services/states/FeatureServer/0/applyEdits'
payload = {'f': 'json', 'updates': '[{"attributes":{"ObjectId":25,"positive":0.9}}]' , 'token': token}

# stitch together, 'objectid' + id
ids_blues = []
ids_reds = []
for k, v in state_ids.iteritems():
    ids_blues.append({'ObjectId': v})
    ids_reds.append({'ObjectId2': v})

# should be parametrized

def resetBlues():
    # have to pass a different objectid each time here
    dataList = []
    lowestColor = {'positive': 0.9}

    # x, y, copy z of x, and update z with y
    # reset to 0 successful
    for obj in ids_blues:
        # mesh two dicts
        attr = lowestColor.copy()
        attr.update(obj)

        # turn this to a str when passing
        dataList.append({'attributes': attr})

        # ready to make request
        payload = {'f': 'json', 'updates': str(dataList) , 'token': token}
        r = requests.post(url_blues, data=payload)
        print r.text


# now for reds, gotta change objectId to 2, ugh.
payload_reds = {'f': 'json', 'updates': '[{"attributes":{"ObjectId2":25,"positive":0.4,"name":"california"}}]' , 'token': token}
url_reds = 'http://services3.arcgis.com/zBkEB8YtoDaCmWOf/arcgis/rest/services/reds/FeatureServer/0/applyEdits'

def resetReds():
    # have to pass a different objectid each time here
    dataList = []
    lowestColor = {'positive': 0.9}

    # x, y, copy z of x, and update z with y
    # reset to 0 successful
    for obj in ids_reds:
        # mesh two dicts
        attr = lowestColor.copy()
        attr.update(obj)

        # turn this to a str when passing
        dataList.append({'attributes': attr})

        # ready to make request
        payload = {'f': 'json', 'updates': str(dataList) , 'token': token}
        r = requests.post(url_reds, data=payload)
        print r.text


# final dict
# format is 'positive': color, 'name': state, object id
scores = getScores();
print 'the scores are ', scores

# separate scores to blue nad red
# scores is a list of objects, with positive, 
def getBlueStates(scores):

     


    return


def updateMap():

    # unlike the resets, only certain items are targeted
    # find the the id of the states

    return









