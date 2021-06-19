from flask import *
from mastodon import Mastodon
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("comment.html")

@app.route("/postmsg",methods = ["POST","GET"])
def postmsg():
    if request.method == "POST":
        try:
            word = request.form["name"]
            url=f"https://ta.wiktionary.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%B1%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AF%81:Search?search={word}&fulltext=%E0%AE%A4%E0%AF%87%E0%AE%9F%E0%AF%81%E0%AE%95&ns0=1"
            page = requests.get(url=url)
            soup = BeautifulSoup(page.content, 'html.parser')
            tamil= soup.find('div',class_="searchresult").text
            
              
        except:
            con.rollback()
            tamil="not Get"
        finally:
            return render_template("get1.html",word=word,tamil=tamil)

@app.route("/postmsg1",methods = ["POST","GET"])
def postmsg1():
    if request.method == "POST":
        try:
            name = request.form["team"]
            
            mastodon = Mastodon(
    
                access_token = 'spxq-ji5UCJ3GCUEvFjart739K6tttG5dlQGog9D7h0',
                api_base_url = 'https://mastodon.social'
            )
            
            mastodon.status_post(str(name))
            msg = "Message succesfully Posted"
                
        except:
            con.rollback()
            msg = "We can not send Message to Mastodon"
        finally:
            return render_template("success.html",msg = msg)            


if __name__ == "__main__":
    app.run(debug = True)  

