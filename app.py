# FLASK_APP=main.py flask run
from flask import Flask, render_template, request
import json
import funtionJson as fJ
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/purpose")
def purpose():
    return render_template('purpose.html')

@app.route("/video")
def readMore():
    return render_template('readMore.html')

@app.route("/curriculum")
def curriculum():
    return render_template('curriculum.html')

@app.route("/apply")
def apply():
    return render_template('apply.html')

@app.route("/sucess", methods=['post'])
def sucess():

    if request.method == "POST": #userarequest.form['user']#전달받은nameluser인데이터
        name = request.form.get ('name')
        stuId = request.form.get ('stuId')
        schedule = request.form.get ('schedule')
        email = request.form.get ('email')
        stuM = request.form.get ('stuM')
        if(stuM == None): stuM = "입력 없음"
        snsId = request.form.get ('snsId')
        if(snsId == None): snsId = "입력 없음"
        print(f"{name} {stuId} {snsId} {email} {schedule} {stuM}")

        # data = fJ.userDataLoad()
        result = {
            "name" : f"{name}",
            "stuId" : f"{stuId}",
            "snsId" : f"{snsId}",
            "email" : f"{email}",
            "schedule" : f"{schedule}",
            "stuM" : f"{stuM}"
        }   

        #data = fJ.userDataLoad()
        #data.append(result)
        fJ.userDataDump(result)
        
        script_path = "excel.py"
        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"오류 발생: {e}")
        
    return render_template('sucess.html' , name=name, stuId=stuId, schedule=schedule, email=email, stuM=stuM, snsId=snsId)