from flask import Flask,render_template,request
'''
It create an instance of the Flask class 
which will be our WSGI(web server Gateway Interface) application 
'''
app = Flask(__name__)
@app.route("/")
def Welcome():
    return "<html><h1>Welcome to the flask courses </h1></html>"

@app.route("/index",methods=['GET'])##IF THIS METHOD IS NOT WRITTEN HERE THEN BY DEFAULT IT IS GET REQUEST 
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.method['name']
        return f'Hello {name}'
    return render_template('form.html')
if __name__=="__main__":
    app.run(debug=True) 
    # this also work fine for us but when we use dubug =True inside the app.run then it automatically provide us hot reloading 