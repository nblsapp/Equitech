from __main__ import app
from flask import Flask, render_template, request,make_response,redirect
import pymongo, dns
import json, os

client = pymongo.MongoClient(os.environ['MONGO'])

db = client.Equitech

members = db.Members

@app.route('/login')
def login():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if request.args.get('path'):
        print(request.args.get('path'))
        return redirect('/login')
    if username == None:
        return render_template('login/index.html')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect('/')
            else:
                found = True
    if found == False:
        return render_template('login/index.html')
    return redirect('/')


@app.route('/password', methods=['POST'])
def main1():
    found = False
    cursor = list(members.find())
  
    for i in cursor:
      if i["email"] == request.form['email']:
        found = True
        break

    if request.form['email'] and found==True:
      resp = make_response(render_template('login/password.html'))
      resp.set_cookie('login', request.form['email'])
      return resp
    else:
      resp = make_response(render_template('login/new_password.html'))
      resp.set_cookie('login', request.form['email'])
      return resp
@app.route('/success')
@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('login', '', expires=0)
    return resp
