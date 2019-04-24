import requests, hashlib

target_url = 'https://xyz.inschool.fi'

WILMA_USERNAME = ''
WILMA_PASSWORD = ''
WILMA_MOBILE_APP_ID = ''

r = requests.get(target_url + '/index_json')

if r.status_code == 200:
    SessionID = r.json()['SessionID']

    apikey_text = WILMA_USERNAME + '|' + SessionID + '|' + WILMA_MOBILE_APP_ID
    hash_text = hashlib.sha1(bytes(apikey_text, 'utf-8')).hexdigest()
    apikey = 'sha1:' + hash_text

    payload = {
        'Login': WILMA_USERNAME,
        'Password': WILMA_PASSWORD,
        'SessionID': SessionID,
        'ApiKey': apikey
        }

    r = requests.post(target_url + '/login', payload, allow_redirects=False)

    if r.status_code == 303:
        home_url = r.headers['Location'].replace('?checkcookie', '')
        jar = r.cookies
        r = requests.get(home_url + '/news/index_json', cookies=jar)
        print(r.json())

