from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='ThisisSecret'

from random import *

def setSession():
    session['target'] = randint(1,101)

@app.route('/')
def index():
    session['display'] = 0
    setSession()
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    inputs = request.form['number']
    input_num = int(inputs)
    try:
        if input_num < session['target']:
            session['display'] = 1
        elif input_num > session['target']:
            session['display'] = 2
        else:
            session['display'] = 3
    except:
        session['display'] = 0

@app.route('/reset',methods=['GET','POST'])
def reset():
    setSession()
    return redirect('/')

app.run(debug=True)
