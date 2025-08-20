##Building Url Dynamically 
##Jinja 2 Template Engine 
##jinja 2 Template Eingine 
'''
{{ }} expressions to print output in html
{%....%} conditions,for loops 
{#....#} this is for comments
'''
from flask import Flask,render_template,request,redirect,url_for
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
@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/success/<int:score>') #here we assign a rule for variable like here we assign a rule for score is int 
def success(score):
    return"The Marks you got is" + str(score)

@app.route('/result/<int:score>') #here we assign a rule for variable like here we assign a rule for score is int 
def result(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html',result=res)


@app.route('/resultscr/<int:score>') #here we assign a rule for variable like here we assign a rule for score is int 
def results(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score':score,"res":res}
    return render_template('result1.html',results=exp)
     
@app.route('/resultif/<int:score>') 
def result1(score):

    return render_template('result2.html',results=score)

@app.route('/submits',methods=['POST','GET'])
def submits():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    return redirect(url_for('resultif',score = total_score))


if __name__=="__main__":
    app.run(debug=True) 
    # this also work fine for us but when we use dubug =True inside the app.run then it automatically provide us hot reloading 