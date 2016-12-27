import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'e36c979ae1b8412588789dcc50d7569d',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age',
})

body = "\"url\":\"http://images.closerweekly.com/uploads/posts/image/87845/sylvester-stallone.jpg\""
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{" + body + "}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
