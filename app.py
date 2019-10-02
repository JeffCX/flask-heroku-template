from flask import Flask,render_template,redirect,request
import os
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html")

@app.route("/match",methods=["POST","GET"])
def gan():
    if request.method=="POST":
        return render_template("index.html",matched = True)









if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
