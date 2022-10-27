from igwn_alert import client
from igwn_alert import IGWNAlertClient
import json

# Ligo allert user guide
# https://emfollow.docs.ligo.org/userguide/

# Library that allow to recive allert from ligo
# https://computing.docs.ligo.org/igwn-alert/client/guide.html
# At this time, access to igwn-alert is limited to LIGO, Virgo, and KAGRA members 
# so i can't procide without a proper LIGO, Virgo, or KAGRA account 

#possible way to convert the json file into xml
#https://stackoverflow.com/questions/8988775/convert-json-to-xml-in-python


def process_alert(topic, payload):
    if topic == 'cbc_gstlal':
        alert = json.loads(payload)
        

client = IGWNAlertClient(group='gracedb-test')
topics = ['superevent', 'cbc_gstlal']
client.listen(process_alert, topics)