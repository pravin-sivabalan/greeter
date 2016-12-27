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

body = "\"url\":\"http://bloximages.newyork1.vip.townnews.com/stltoday.com/content/tncms/assets/v3/editorial/2/05/2058e5ee-ef90-11e5-8d8e-cbd9245f0029/56f039262c7f3.image.jpg?resize=1200%2C1309\""
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{" + body + "}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
