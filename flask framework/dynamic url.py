from flask import Flask,render_template,request , redirect , url_for

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score , 'result':res}

    return render_template("result1.html", result=exp)


@app.route('/submit',methods=['GET','POST'])
def submit():
    total_submit=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])

        total_submit=science + maths / 2 

    return redirect(url_for('successres',score=total_score))


