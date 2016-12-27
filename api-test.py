import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '53a06343003643058b0e4d6f407b6d59',
}

params = urllib.urlencode({
    'isIdentical' : 'true',
    'confidence' : '5'
})

body = {
    "faceId1":"f0a1dfae-b326-4ca8-8f5a-fbefacd7b7cd",
    "faceId2":"5ec0c153-5093-4863-8d76-aa055c313cbb"
}

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/verify?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("oh oh")
    # print("[Errno {0}] {1}".format(e.errno, e.strerror))
