import speech_recognition as sr
import webbrowser
import pyttsx3
import requests  # For Spotify API calls
import musicly
import os
import json

recognizer = sr.Recognizer()
engine = pyttsx3.init()


CLIENT_ID = '9e8dc82b47ea4f62a94f63a1bfa07fd7'
CLIENT_SECRET = 'c751f6458d5745f9866d864cb67d67ad'
REDIRECT_URI = 'http://localhost:8080/callback'


TOKEN_FILE = 'access_token.json'


def get_auth_token():
    auth_url = f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=user-modify-playback-state user-read-playback-state streaming"
    print("Please log in to Spotify by visiting this URL:")
    print(auth_url)
    webbrowser.open(auth_url)
    auth_code = input("Enter the code from the URL after logging in: ")
    return auth_code


def get_access_token(auth_code):
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(token_url, data=payload)
    response_data = response.json()
    
    
    if "access_token" in response_data:
        return response_data
    else:
        print(f"Error getting access token: {response_data}")
        raise Exception("Failed to get access token.")



def save_access_token(access_token):
    with open(TOKEN_FILE, 'w') as f:
        json.dump({"access_token": access_token}, f)


def load_access_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            data = json.load(f)
            return data.get("access_token")
    return None


def refresh_access_token(refresh_token):
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(token_url, data=payload)
    return response.json()


def search_song(song_name, access_token):
    search_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"q": song_name, "type": "track", "limit": 1}
    response = requests.get(search_url, headers=headers, params=params)
    tracks = response.json().get("tracks", {}).get("items", [])
    if tracks:
        return tracks[0]["uri"]
    return None


def play_song(song_uri, access_token):
    play_url = "https://api.spotify.com/v1/me/player/play"
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {"uris": [song_uri]}
    response = requests.put(play_url, headers=headers, json=payload)

    print(f"Play song response status code: {response.status_code}")
    if response.status_code != 204:
        print(f"Error details: {response.json()}")
        return False
    return True



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        # Extract the song name from the command
        song_name = c[5:].strip().lower()

        
        if song_name in musicly.music:
            webbrowser.open(musicly.music[song_name])
            speak(f"Playing {song_name} from your library.")
        else:
           
            try:
                access_token = load_access_token()

                
                if not access_token:
                    auth_code = get_auth_token()
                    token_response = get_access_token(auth_code)
                    access_token = token_response.get("access_token")
                    refresh_token = token_response.get("refresh_token")
                    save_access_token(access_token)
                    print("Access Token saved.")

                song_uri = search_song(song_name, access_token)
                if song_uri:
                    if play_song(song_uri, access_token):
                        speak(f"Playing {song_name} on Spotify.")
                    else:
                        speak("Failed to play the song on Spotify.")
                else:
                    speak(f"Sorry, I couldn't find the song '{song_name}' on Spotify.")
            except Exception as e:
                print(f"Error with Spotify integration: {e}")
                speak("There was an error with Spotify integration.")


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Hello, how may I assist you?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")

