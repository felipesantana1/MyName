from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def displayFom():
    return render_template('formPage.html')

@app.route('/process', methods=['POST'])

def createUser():
    y = request.form['name']
    print y
    return redirect('/')

app.run(debug=True)