getpost.py
@app.route('/successif/<int:score>')
def successif(score):
     res=""
     return render_template('result.html',result=score)




if __name__ == "__main__":
    app.run(debug=True)


result.html
<h1>
    based on the marks , u have scored {{result}}

    {% if result>=50 %}
    <h1>you have passed with marks {{result}}</h1>
    {% else %}
    <h1>you have failed with {{result}}</h1>
    {% endif %}

</h1>
     
