from flask import Flask, render_template, request, redirect
from datetime import date
from age import age
from catCalc import catCalc
from dogCalc import dogCalc

app = Flask(__name__)
#pet array type of pet ,name, dob

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/generate", methods=["POST"])
#def generate():
#   return redirect("/download")

@app.route("/download", methods=["POST"])
def download():
    pet = []
    name = request.form.get("petName")
    dob = request.form.get("dob")
    petType = request.form.get("petType")
    dobSplit = dob.split("-")
    #dobSplitFormat = (int(dobSplit[0]),int(dobSplit[1]), int(dobSplit[2]))
    realDob = age(date(int(dobSplit[0]),int(dobSplit[1]), int(dobSplit[2])))
    if petType == "cat":
        petAge = catCalc(realDob)
    else:
        petAge = dogCalc(realDob)
    
    pet.append(name)
    pet.append(dob)
    pet.append(petType)
    pet.append(realDob)
    pet.append(petAge)
    #pet.append(dobSplitFormat)

    return render_template("download.html",pet = pet)


 
