import base64

def encodeToB6(val):
    return str( base64.b64encode( bytes(val,'utf8')))
    