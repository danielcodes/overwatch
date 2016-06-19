"""request to update all the states to a level ground of 0.4
   to send request, the object id of the state is needed, so created a dict with (state => id)
"""

import requests

token = '9uoHmj0khoGE-IPi0suBX32onwoIAsSJzSZwpB1MKv8v5gwYkP382gLLNop5tA__HFQP-SX14R8h11vY6cXqKup_gH1zNs7CY4CIcK9wDCEJkejdMCtjNCfwAftlMpLqQOfEewk6nC_uMLOrWgUGJw..' 

payload = {'f': 'json', 'updates': '[{"attributes":{"ObjectId":25,"positive":0.9,"name":"california"}}]' , 'token': token}
url = 'http://services3.arcgis.com/zBkEB8YtoDaCmWOf/arcgis/rest/services/states/FeatureServer/0/applyEdits'

r = requests.post(url, data=payload)
print r
print r.text



