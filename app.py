from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p>PIZZA!</p>"
if(__name__=="__main"):
   app.run(debug=False)
