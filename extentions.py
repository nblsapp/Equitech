from __main__ import app
from flask import Flask, render_template, request,make_response,redirect
import json 
@app.route('/extentions')
def extentions():
  mail = request.cookies.get('login')
  username = request.cookies.get('login')
  psw = request.cookies.get('psw')
  if username==None:
    return redirect('/login')
  with open('static/json/members.json') as a:
    a = json.load(a)
  found = False
  for i in a:
    if i["email"] == username:
      if i["password"] != psw:
        return redirect('/login')
      else:
        found = True
  if found == False:
    return redirect('/login')
  return render_template('extentions/index.html')