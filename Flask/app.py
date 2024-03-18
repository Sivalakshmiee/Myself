from flask import Flask, redirect, url_for
# #WSGI APPLICATION

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>hello everyone</h1>'


#BUILDING A DYNAMIC URL
@app.route("/sucess/<int:score>")
def sucess(score):
    return 'passed: the  score is  ' + " " + str(score)

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

if __name__ == '__main__':
    app.run(debug=True)

