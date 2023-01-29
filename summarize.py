import requests
def summarize(text):
    url = "https://api.meaningcloud.com/summarization-1.0"
    payload = {'key': '06d3f9ebef2a5490af27b80ee6a4d316', 'sentences':'8'}
    payload['txt'] = text
    response = requests.post(url, data=payload)
    print(response.json())
    return response.json()["summary"]