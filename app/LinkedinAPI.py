from flask import session
import base64
import requests
from pprint import pprint
import oauth2

CLIENT_ID = '86faisvke7rqht'
CLIENT_SECRET = 'vfywuq3lwEUUqzU2'
REDIRECT_URI = 'http://localhost:5000/index' #need to direct them to our main page

# OAuth endpoints given in the LinkedIn API documentation  
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization' #endpoint
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'  

# Exchange Authorization Code for an Access Token
def authorizeLinkedIn(code):
    code=code
    print ('-------- CODE ------------', code)
    data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
    }

    unencodedAuthHeader = CLIENT_ID+':'+CLIENT_SECRET
    encodedHeader = base64.b64encode(unencodedAuthHeader)

    headers = {
    'Authorization': 'Basic '+encodedHeader
    }

    response = requests.post(token_url, data=data, headers=headers)
    decodedResponse = response.json()

    print('------- FULL REPONSE -------')
    print(response)

    print('------- SPOTIFY TOKEN RESPONSE -------')
    print(decodedResponse)

    # SET USER SESSION WITH SPOTIFY ACCESS TOKEN & REFRESH TOKEN
    access_token = decodedResponse['access_token']
    refresh_token = decodedResponse['refresh_token']
    expires_in = decodedResponse['expires_in']

    responseToken = {}
    responseToken['access_token'] = access_token
    responseToken['refresh_token'] = refresh_token
    responseToken['expires_in'] = expires_in
    
    print('------- RESPONSE TOKEN -------')
    print(responseToken)
    return responseToken

# def getSpotifyPlaylists(access_token):
#     # Initialize an object in which to store playlist data
#     playlistsObj = {'data': []}

#     # Set API headers
#     headers = {
#     'Authorization': 'Bearer ' + access_token
#     }

#     # Set API params
#     params = {
#         'limit': 50
#     }

#     # API endpoint
#     endpoint = 'https://api.spotify.com/v1/me/playlists'

#     # Call API
#     try:
#         response = requests.get(endpoint, params=params, headers=headers)
#         decodedResponse = response.json()
#         print('------- FULL DECODED RESPONSE -------')
#         pprint(decodedResponse)

#         for playlist in decodedResponse['items']:
#             tempPlaylist = {}
#             tempPlaylist['name'] = playlist['name']
#             try:
#                 tempPlaylist['image'] = playlist['images'][0]['url']
#             except:
#                 tempPlaylist['image'] = ''
#             tempPlaylist['tracksUrl'] = playlist['tracks']
#             playlistsObj['data'].append(tempPlaylist)
#             #print tempPlaylist
#         return playlistsObj

#     except Exception as e:
#         print
#         print('------- ERROR GETTING PLAYLIST DATA FROM SPOTIFY API -------', e)
#         print
