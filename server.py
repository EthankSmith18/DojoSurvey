from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/process', methods=['post'])
def process():
    session['name'] = request.form['name']
    session['school'] = request.form['school']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    is_valid = True
    if len(session['name']) < 1:
        flash("Please enter a Name")
        is_valid = False
    if len(session['school']) < 1:
        flash("Please enter a School")
        is_valid = False
    if len(session['language']) < 1:
        flash("Please enter a Language")
        is_valid = False
    if len(session['comment']) < 1:
        flash("Please enter a Comment")
        is_valid = False
    if not is_valid:
        return render_template('/index.html')
    else:
        return redirect('/results')

@app.route('/results')
def results():
    return render_template('/results.html')





if __name__=="__main__":
    app.run(debug=True) 