import requests
import credentials #importing credentials from another file

CLIENT_ID = credentials.id
CLIENT_SECRET = credentials.secret

TOKEN_URL = 'https://accounts.spotify.com/api/token'
AUTH_URL = 'https://accounts.spotify.com/authorize'

# let's authorize
auth_response = requests.get(AUTH_URL, {
	'client_id' : CLIENT_ID,
	'response_type' : 'code',
	'redirect_uri' : 'https://xd,',
	'scope' : 'user-read-currently-playing',
	})

print(auth_response.url)

# HOW DO YOU GET THE CODE FROM THE REDIRECTED GET REQUEST?
#code = auth_response_data['code']

token_response = requests.post(TOKEN_URL, {
	'grant_type' : 'authorization_code',
	'code' : code,
	'redirect_uri' : 'https://xd',
	'client_id' : CLIENT_ID,
	'client_secret' : CLIENT_SECRET,
	})

# convert the response to JSON
token_response_data = token_response.json()

# save the access token
access_token = token_response_data['access_token']
#print(access_token)
# create a header with our access token
headers = {
	'Authorization': 'Bearer {token}'.format(token=access_token)
}


# get the now playing song
NP_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

np_response = requests.get(NP_URL, headers=headers)

np_json = np_response.json()

print(np_json)