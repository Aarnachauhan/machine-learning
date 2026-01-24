GET request
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

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)


------------------------------------------------------
POST REQUEST

from flask import Flask,render_template,request
#flask is package and Flask is 

'''
It creates an instance of the Flask class,
which will be the WSGI (Web Server Gateway Interface) application
'''

app = Flask(__name__)   # ✅ __name__ is REQUIRED

@app.route("/")
def welcome():
    return "<html><h1>welcome to the html design</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f" this is user name = {name}"
    return render_template("form.html") #else statement
if __name__ == "__main__":
    app.run(debug=True)



form.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>submit your form</h1>
    <form method="post">
    <label for="name"> name </label>
    <input name="name" id="name" type="text">
    <input value="submit" type="submit">
    </form>
</body>
</html>



