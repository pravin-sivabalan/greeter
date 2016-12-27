import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '53a06343003643058b0e4d6f407b6d59',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/verify?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
