from __main__ import app
from flask import Flask, render_template, request,make_response,redirect
import json 
@app.route('/account')
def profile():
  mail = request.cookies.get('login')
  if mail==None:
    return redirect('/login')
  
  with open('static/json/members.json') as file:
    file = json.load(file)
  with open('static/json/bio.json') as file2:
    file2 = json.load(file2)
  try:
    bio = file2[mail]
  except:
    bio = ''

  for i in range(0,len(file)):
    if file[i]["email"]==mail:
      break
  
  user = file[i]
  username = user["username"]
  name = user["first"]+' '+user["last"]
  return render_template('profile.html',name=name,username=username, mail=mail, bio=bio)
@app.route('/account',methods=['POST'])
def profile2():
  mail = request.cookies.get('login')
  with open('static/json/bio.json') as file2:
    file2 = json.load(file2)
  a = request.form['bio']
  file2[mail]=a
  with open('static/json/bio.json','w') as out:
    json.dump(file2,out)
  return redirect('/account')