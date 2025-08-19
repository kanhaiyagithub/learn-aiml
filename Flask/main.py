from flask import Flask,render_template
'''
It create an instance of the Flask class 
which will be our WSGI(web server Gateway Interface) application 
'''
app = Flask(__name__)
@app.route("/")
def Welcome():
    return "<html><h1>Welcome to the flask courses </h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True) 
    # this also work fine for us but when we use dubug =True inside the app.run then it automatically provide us hot reloading 