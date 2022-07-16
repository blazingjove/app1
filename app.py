from flask import Flask, render_template, request, redirect
from datetime import date
import logging
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
    if realDob > 15:
      return render_template("/generate.html");
    elif petType == "cat":
        petAge = catCalc(realDob);
        doggie = "cat";
    elif petType == "small":
        petAge = dogCalc(realDob,petType)
        doggie = "dog";
        petType = "small dog";
    elif petType == "medium":
        petAge = dogCalc(realDob,petType)
        doggie = "dog";
        petType = "medium dog"
    elif petType == "large":
        petAge = dogCalc(realDob,petType)
        doggie = "dog";
        petType = "large dog"
    else:
        petAge = dogCalc(realDob,petType)
        doggie = "dog";
        petType = "giant dog" 
        
    pet.append(name)
    pet.append(dob)
    pet.append(petType)
    pet.append(realDob)
    pet.append(petAge)
    pet.append(doggie)
    #pet.append(dobSplitFormat)

    return render_template("download.html",pet = pet)

if __name__ =="__main__":
  app.run()
 
