from flask import Flask , render_template , request
import urllib
import random
import json
app = Flask(__name__)


@app.route("/")
def home():
    print("HELLO I AM A FLASK APP")
    movieName = ["Avengers" , "Don" , "India" , "Space"]
    myMovieName = random.choice(movieName)
    query = random.choice(["Avengers" , "Don" , "India" , "Space" , "Cricket"  , "Mera Badla" , "DJ"])
    try:
        url =  f"http://www.omdbapi.com/?s={myMovieName}&apikey=c4b3701e"
        response = urllib.request.urlopen(url)
        data = response.read()
        jsonData = json.loads(data)["Search"]
        return render_template("index.html" , page_name = "Movie Mania" , movieList  = jsonData , query =query)
    except Exception as e:

        return render_template("index.html" , page_name = page_name)


@app.route("/search" , methods = ['GET'])
# GET  - Insecure ( Search )
# POST - Secure (Password , Credit Number )
def search_results():
    movieName  =  request.args.get("Moviequery")
    movieName = movieName.strip()
    try:
        url =  f"http://www.omdbapi.com/?s={movieName}&apikey=c4b3701e"
        url = url.replace(" ", "%20")
        response = urllib.request.urlopen(url)
        data = response.read()
        jsonData = json.loads(data)["Search"]
        return render_template("index.html" , page_name = "Movie Mania" , movieList = jsonData , query = movieName)
    except Exception as e:
        print(e)
        return f"NO INTERNET CONNECTION {e}"

app.run(debug=True)


