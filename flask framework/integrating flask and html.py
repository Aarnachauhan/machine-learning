main.py file :


from flask import Flask
#flask is package and Flask is 

'''
It creates an instance of the Flask class,
which will be the WSGI (Web Server Gateway Interface) application
'''

app = Flask(__name__)   # ✅ __name__ is REQUIRED

@app.route("/")
def welcome():
    return "<html><h1>welcome to the html design</h1></html>"

if __name__ == "__main__":
    app.run(debug=True)
-------------------------------------------------------------------------------
from flask import Flask,render_template
#flask is package and Flask is 

'''
It creates an instance of the Flask class,
which will be the WSGI (Web Server Gateway Interface) application
'''

app = Flask(__name__)   # ✅ __name__ is REQUIRED

@app.route("/")
def welcome():
    return "<html><h1>welcome to the html design</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)


------------------------------------------------
it will go inside template folder and then find for the desired html file 
