from flask import Flask
'''
It create an instance of the Flask class 
which will be our WSGI(web server Gateway Interface) application 
'''
app = Flask(__name__)
@app.route("/")
def Welcome():
    return "Welcome to this Flask Course and this course should be amazing and i belive that krish naik will deliver that quality"

if __name__=="__main__":
    app.run(debug=True) 
    # this also work fine for us but when we use dubug =True inside the app.run then it automatically provide us hot reloading 