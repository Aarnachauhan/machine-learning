getpost.py

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score , 'result':res}

    return render_template("result1.html", result=exp)
if __name__ == "__main__":
    app.run(debug=True)


result1.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>
        final results
    </h1>
    <table border=2 >
        {% for key,value in result.items() %}
        <tr>
            {# this is the comment #}
            <th>{{key}}</th>
            <th>{{value}}</th>

        {% endfor %}
        </tr>

    </table>
</body>
</html>
