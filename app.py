from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def ncd_rac():
    if request.method == "POST":
        total=0
        age = int(request.form['age'])
        smoke = int(request.form['smoke'])
        alcohol = int(request.form['alcohol'])
        waist = int(request.form['waist'])
        phy_act = int(request.form['phy_act'])
        fam_his = int(request.form['fam_his'])

        if (request.form['age']== None):
            return redirect(url_for('fail',str="Please enter all the values."))
        if (request.form['smoke']== None):
            return redirect(url_for('fail',str="Please enter all the values."))
        if (request.form['alcohol']== None):
            return redirect(url_for('fail',str="Please enter all the values."))
        if (request.form['waist']== None):
            return redirect(url_for('fail',str="Please enter all the values."))
        if (request.form['phy_act']== None):
            return redirect(url_for('fail',str="Please enter all the values."))
        if (request.form['fam_his']== None):
            return redirect(url_for('fail',str="Please enter all the values."))    

        total = age + smoke + alcohol + waist + phy_act + fam_his

        res=""
        
        if total>4:
            res="The person may be at higher risk of NCDs and needs to be prioritized for attending screening."
        else:
            res="The person is not at risk of NCDs and doesn't need screening."
               
    return render_template('result.html',result=res,total=total, age=age,smoke=smoke,alcohol=alcohol,
                           waist=waist,phy_act=phy_act,fam_his=fam_his)
    
'''@app.route('/success/<int:score>')
def success(score):
    res=""
    #print(score)
    if score>4:
        res="The person may be at higher risk of NCDs and needs to be prioritized for attending screening."
    else:
        res="The person is not at risk of NCDs and doesn't need screening."

    return render_template('result.html',result=res,sc=score)'''

@app.route('/fail/<string:str>')
def fail(str):
    return render_template('error.html',str=str)

@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)