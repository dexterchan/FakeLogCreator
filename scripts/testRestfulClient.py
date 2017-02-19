'''
Created on Feb 19, 2017

@author: dexter
'''

import json
import time
import datetime
import httplib2

if __name__ == '__main__':

    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     ="application/json"

    url = "http://ec2-54-208-51-43.compute-1.amazonaws.com:8082/queryIncidentFromLog"

    data = {
        "ISO_DATE": "2016-12-30 16:27:54,435", 
        "MESSAGE": "FxRestfulController: USDUSD not found: ccy1 and ccy2 should not be the same FxRestfulController.java 208 ", 
        "STATUS": "OK"
    }
    

    headers = {'Content-Type': content_type_header}
    print ("Posting %s" % data)

    while True:
        response, content = http.request( url,
                                          'POST',
                                          json.dumps(data),
                                          headers=headers)
        print (response)
        print (content)
        time.sleep(3)