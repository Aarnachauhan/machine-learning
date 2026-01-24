jinja.py

#this is expression to put output in html = {{}}
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template("result.html", result=res)
if __name__ == "__main__":
    app.run(debug=True)

result.html
<h1>
    based on the marks , u are {{result}}
</h1>


http://127.0.0.1:5000/success/90
o/p
based on the marks , u are PASSED

-----------------------------------

#2 condition template
{%...%}

#3 comment 
{# #}
--------------------------------------
  
