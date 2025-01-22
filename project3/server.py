from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def spotify_callback():
    auth_code = request.args.get('code')
    if auth_code:
        return f"Authorization code received: {auth_code}", 200
    return "No authorization code received", 400

if __name__ == '__main__':
    app.run(port=8080)
