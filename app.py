from flask import Flask,render_template,request
import numpy as np
import pickle
with open("Loan_Prediction.pkl",'rb')as f:
    model=pickle.load(f)
#create an object instance
app=Flask(__name__)
@app.route('/home')
def check():
    return "Iam pasala ganesh from NBKRIST"
@app.route('/')  #by default methods=['GET']
def new():
    
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    #check the model with input samoles
    gender = int(request.form['gender'])
    applicant_income=int(request.form['applicant_income'])
    coapplicant_income=float(request.form['coapplicant_income'])
    loan_amount=float(request.form['loan_amount'])
    term = float(request.form['loan_term'])
    credit_history=float(request.form['credit_history'])
    property_area=int(request.form['property_area'])
    married=int(request.form['married'])
    dependent=int(request.form['dependents'])
    education=int(request.form['education'])
    self_employed=int(request.form['self_employed'])



    user_input = np.array([[gender,applicant_income,coapplicant_income,loan_amount,term,
                        credit_history,property_area,married,dependent,education,self_employed]])
    #user_input
    prediction = model.predict(user_input)[0]
    if prediction==1:
        prediction="Loan will be Approved"
        return render_template('index.html',prediction=prediction)

    else:
        prediction="Loan is Rejected"
        return render_template('index.html',prediction=prediction)


app.run(debug=True,use_reloader=True)
