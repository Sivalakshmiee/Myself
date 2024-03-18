from flask import Flask, redirect, url_for,render_template,request
# #WSGI APPLICATION

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


#BUILDING A DYNAMIC URL
@app.route("/sucess/<int:score>")
def sucess(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score':score, 'res':res}
    return render_template('result.html', result=exp)

@app.route("/fails/<int:score>")
def fails(score):
    return 'failed: the  score is  ' + str(score)

#result checker
@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result= "sucess"

    #return  results
    return redirect(url_for(result,score=marks))

#result checker html
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        dsa=float(request.form['dsa'])
        tc=float(request.form['tc'])
        total_score=(maths + science + dsa + tc) / 4

    res = ""
    if total_score >= 50:
        res="sucess"
    else:
        res="fails"   

    return redirect(url_for('sucess', score=total_score)) 


if __name__ == '__main__':
    app.run(debug=True)

