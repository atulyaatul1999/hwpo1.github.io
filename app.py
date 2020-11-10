from flask import Flask,render_template,request
import joblib

lr=joblib.load('hard_work_paysoff_model.pkl')
# print(lr.predict([[3]]))
# print("done")


app=Flask(__name__)

@app.route('/')
def new_fun():
    return render_template('index.html')


@app.route('/submit',methods=['post','get'])
def get_hours():
    if request.method=='POST':
        n=float(request.form['hours'])
        marks=lr.predict([[n]])
        print(marks[0][0])
        return render_template('index.html',marks=marks[0][0])


if __name__=='__main__':
    app.run(debug=True)