#basic skeleton of the flask framework


from flask import Flask
#flask is package and Flask is 

'''
It creates an instance of the Flask class,
which will be the WSGI (Web Server Gateway Interface) application
'''

app = Flask(__name__)   # ✅ __name__ is REQUIRED

@app.route("/")
def welcome():
    return "Welcome to this Flask skeleton"

if __name__ == "__main__":
    app.run(debug=True) #because of this debug , server will start on its own . just save the file
    





