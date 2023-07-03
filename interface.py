from flask import Flask,render_template,request,jsonify
from utils import HeartData
import config

app=Flask(__name__)

@app.route('/')
def get_home_page():
    return render_template('heart.html')

@app.route('/predict_class',methods=["GET","POST"])
def get_predict_class():
    if request.method=="GET":
        data=request.args.get
        print("Data",data)
        age=eval(data('age'))
        sex=eval(data('sex'))
        cp=eval(data('cp'))
        trestbps=eval(data('trestbps'))
        chol=eval(data('chol'))
        fbs=eval(data('fbs'))
        restecg=eval(data('restecg'))
        thalach=eval(data('thalach'))
        exang=eval(data('exang'))
        oldpeak=eval(data('oldpeak'))
        slope=eval(data('slope'))
        ca=eval(data('ca'))
        thal=eval(data('thal'))
        heart=HeartData(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        predict_class=heart.get_predicted_class()
        return render_template("heart.html",prediction=predict_class)
    
    if request.method=="POST":
        data=request.form
        print("Data",data)
        age=data['age']
        sex=data['sex']
        cp=data['cp']
        trestbps=data['trestbps']
        chol=data['chol']
        fbs=data['fbs']
        restecg=data['restecg']
        thalach=data['thalach']
        exang=data['exang']
        oldpeak=data['oldpeak']
        slope=data['slope']
        ca=data['ca']
        thal=data['thal']
        heart=HeartData(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        predict_class=heart.get_predicted_class()
        return render_template("heart.html",prediction=predict_class)




if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)