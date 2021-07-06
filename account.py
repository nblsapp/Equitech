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
  return render_template('account/index.html',name=name,username=username, mail=mail, bio=bio)
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
@app.route('/premium')
def premium():
  return render_template('account/premium.html')
@app.route('/account/education')
def school():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/')
  listy=[]
  with open('static/schools.txt') as listy:
    listy=listy.readlines()
  for i in range(0,len(listy)):
    listy[i]=[listy[i][7:len(listy[i])],str(i+1)]
  return render_template('account/education.html',listy=listy)
@app.route('/account/connections')
def connection():
  return render_template('account/connection.html')
@app.route('/account/community')
def connectionsacc():
  return render_template('account/community.html')

@app.route('/account/security')
def security():
  return render_template('account/security.html')

@app.route('/account/appearance')
def appearance():
  return render_template('account/appearance.html')

@app.route('/account/advanced')
def advanced():
  return render_template('account/advanced.html')
@app.route('/account/lang')
def lang():
  return render_template('account/lang.html')


@app.route('/account/text')
def text():
  return render_template('account/text.html')
@app.route('/account/logs')
def logs():
  return render_template('account/logs.html')