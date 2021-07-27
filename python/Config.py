subscription_key = "f281ed618eb4492c87dd9bb68f288dae"
face_api_url = 'https://identify-face-ip-r.cognitiveservices.azure.com/face/v1.0/detect'
face_api_url_verify = 'https://identify-face-ip-r.cognitiveservices.azure.com/face/v1.0/verify'

def config():
    print("Call Config")
    return subscription_key, face_api_url, face_api_url_verify

