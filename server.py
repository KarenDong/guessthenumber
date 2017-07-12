from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='ThisisSecret'

from random import *

def setSession():
    if 'target' not in session:
        session['target'] = randint(1,101)

@app.route('/')
def index():
    setSession()
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    try:
        session['display']
    except:
        session['display'] = 0
    inputs = request.form['number']
    input_num = int(inputs)
    if input_num < session['target']:
        session['display'] = 1
    elif input_num > session['target']:
        session['display'] = 2
    else:
        session['display'] = 3

@app.route('/reset',methods=['GET','POST'])
def reset():    
    session['target'] = randint(1,101)
    setSession()
    session['display'] = 0
    return redirect('/')

app.run(debug=True)
