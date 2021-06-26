from __main__ import app
from flask import Flask, render_template, request,make_response,redirect
import json
import random

@app.route('/community')
def servers():
  import re
  def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
  username = request.cookies.get('login')
  with open('static/json/servermembers.json','r') as file:
    file = json.load(file)
  with open('static/json/servers.json','r') as file2:
    file2 = json.load(file2)
  status = True
  servers = []
  servers2 = []
  try:
    servers = file[username]
  except:
    status = False
  if status==True:
    for i in range(0,len(file2)):
      temp = file2[i][6]
      if username in temp:
          servers2.append([deEmojify(file2[i][0]),file2[i][1],file2[i][-1]])
  return render_template('community/index.html',status=status,servers=servers2)
@app.route('/community',methods=['POST'])
def servers1():
  found = False
  name=request.form['name']
  digits=['a','b','c','d','e','f','g','h','i','j','k','l','m','n' 'o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z','1','2','3','4','5','6','7','8','9','0']
  link=''
  for i in range(0,7):
    link+=(random.choice(digits))
  username=request.cookies.get('login')
  with open('static/json/members.json','r') as file:
    file=json.load(file)
  account='Unknown'
  for i in file:
    if i["email"]==username:
      account=i["username"]
  thing=[name,'https://testpreparer.gq/invite/'+link,[],[],[],[],[],account]
  with open('static/json/servers.json','r') as file:
    file=json.load(file)
  file.append(thing)
  with open('static/json/servers.json','w') as out:
    file=json.dump(file,out,indent=4)
  return redirect(f'https://testpreparer.gq/invite/{link}')



@app.route('/invite/<code>')
def invite(code):
  with open('static/json/servers.json','r') as file:
    file=json.load(file)
  
  
  found=False
  for i in range(0,len(file)):
    if file[i][1][31:len(file[i][1])]==code:
      found=True
      name=file[i][0]
      join = file[i][-1]
    
  if found==False:
    return render_template('join.html',vaild=False)
  username = request.cookies.get('login')
  
  
  return render_template('join.html',valid=True,name=name,username=username,join=join)


@app.route('/invite/<code>',methods=['POST'])
def invite2(code):
  username=request.cookies.get('login')
  
  with open('static/json/servers.json','r') as file:
    file=json.load(file)
  found=False
  for i in range(0,len(file)):
    if file[i][1][31:len(file[i][1])]==code:
      server=file[i][0]
      if username not in file[i][-2]:
        file[i][-2].append(username)
      messages = file[i][-3]
      if len(messages) == 0:
        messages.append(['System','No Current Messages'])
  
  if request.cookies.get('login') == None:
    return render_template('claim.html',server=server,username=request.form['name'],check=str('/invite/')+str(code))
  
  with open('static/json/servers.json','w') as out:
    json.dump(file,out,indent=4)
  with open('static/json/servermembers.json','r') as sm:
    sm=json.load(sm)
  try:
    if code not in sm[username]:
      sm[username].append(code)
  except:
    sm[username] = [code]
  with open('static/json/servermembers.json','w') as out:
    json.dump(sm,out,indent=4)
  return render_template('inweb.html',server=server,name=request.form['name'],username=request.cookies.get('login'),stuff='height:'+str(30*40)+';',messages=messages,link=code)

@app.route('/submit/<code>',methods=['POST'])
def submit2(code):
  username=request.cookies.get('login')
  with open('static/json/members.json','r') as file:
    file=json.load(file)
  name='Unknown'
  for i in file:
    if i["email"]==username:
      name=i["username"]
  
  with open('static/json/servers.json','r') as file:
    file=json.load(file)
  found=False
  for i in range(0,len(file)):
    if file[i][1][31:len(file[i][1])]==code:
      messages = file[i][-3]
      messages.append([name,request.form['message']]) #.replace('<p>','').replace('<strong>','').replace('<em>','').replace('<span style="text-decoration: underline;">','').replace('</p>','').replace('</span>','').replace('</em>','').replace('</strong>','')
  with open('static/json/servers.json','w') as out:
    json.dump(file,out,indent=4)
  ####SAME
  username=request.cookies.get('login')
  
  with open('static/json/servers.json','r') as file:
    file=json.load(file)
  found=False
  for i in range(0,len(file)):
    if file[i][1][31:len(file[i][1])]==code:
      server=file[i][0]
      file[i][-2].append(username)
      messages = file[i][-3]
      if len(messages) == 0:
        messages.append(['System','No Current Messages'])
  
  if request.cookies.get('login') == None:
    return render_template('claim.html',server=server,username='Unknown',check=str('/invite/')+str(code))
  
  with open('static/json/servers.json','w') as out:
    json.dump(file,out,indent=4)
  return render_template('inweb.html',server=server,name='Unkown',username=request.cookies.get('login'),stuff='height:'+str(30*40)+';',messages=messages,link=code)