import tekore as tk

def authorize():
 CLIENT_ID = "968ff64455024568a8e12237b905f6ca"
 CLIENT_SECRET = "d4e22db1419b46ae91f6c1ed8cee9091"
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token)