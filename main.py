from flask import Flask, render_template, request,make_response,redirect,flash, url_for
from flask_mail import Mail, Message
app = Flask(__name__)
mail= Mail(app)
import json
import os
import random
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testpreparergq@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('psw')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
@app.errorhandler(500)
def page_not_found1(e):
	return render_template('500.html'), 500

@app.route('/cookies')
def cookies():
  return render_template('cookies.html')


@app.route('/disclaimer')
def disclaimer():
  return "DISCLAIMER: TestPreparer was created by students at  Basis Independent Silicon Valley in San Jose, CA, but is in no way affiliated with the school or it's faculty and staff. We welcome feedback from our users and are actively working on features and improvements."


@app.route('/servers')
def servers():
  return render_template('server.html')



@app.route('/servers',methods=['POST'])
def servers1():
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
  return ('Your link is <a href="https://testpreparer.gq/invite/'+link+'">https://testpreparer.gq/invite/'+link+'</a>')


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
      file[i][-2].append(username)
      messages = file[i][-3]
      if len(messages) == 0:
        messages.append(['System','No Current Messages'])
  
  if request.cookies.get('login') == None:
    return render_template('claim.html',server=server,username=request.form['name'],check=str('/invite/')+str(code))
  
  with open('static/json/servers.json','w') as out:
    json.dump(file,out,indent=4)
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
@app.route('/logout')
def logout():
  resp = make_response(redirect('/'))
  resp.set_cookie('login', '', expires=0)
  return resp


@app.route('/tos')
def tos():
  return render_template('tos.html')


@app.route('/static/json/<file>')
def protect(file):
  return render_template('404.html')


@app.route('/edit')
def edit():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  from os import walk

  with open('static/json/courses.json') as file:
    f=json.load(file)
  new=[]
  for i in range(0,len(f)):
    if f[i][3].strip()==username.strip():
      new.append([f[i][0],str(i)])
  return render_template('edit.html',new=new)


@app.route('/edit',methods=['POST'])
def edit2():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  from os import walk

  with open('static/json/courses.json') as file:
    f=json.load(file)
  new=[]
  for i in range(0,len(f)):
    if f[i][3].strip()==username.strip():
      new.append([f[i][0],str(i)])
  with open("static/json/main.json", "r") as read_file:
    data = json.load(read_file)
  name=request.form['name']
  url=request.form['url']
  type1=request.form['type']
  course=request.form['course']
  category=request.form['category']
  
  user = request.cookies.get('login')
  data.append({"name":name,
    "url":url,
    "type":type1,
    "course":course,
    "category":category,
    "user":user})
  with open("static/json/main.json", "w") as write_file:
    json.dump(data, write_file,indent=4)
  return render_template('edit.html',entered=True,url=url,type=type1,course=course,category=category,name=name,new=new)


@app.route('/school')
def school():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/')
  listy=[]
  with open('static/schools.txt') as listy:
    listy=listy.readlines()
  for i in range(0,len(listy)):
    listy[i]=[listy[i][7:len(listy[i])],str(i+1)]
  return render_template('school.html',listy=listy)


@app.route('/school/<id>')
def school1(id):
  username = request.cookies.get('login')
  if username==None:
    return redirect('/')
  listy=[]
  with open('static/schools.txt') as listy:
    listy=listy.readlines()
  id=int(id)
  id=id-1
  school=listy[id]
  id=id+1
  id=str(id)
  return render_template('myschool.html',school=school,id=id)


@app.route('/school/<id>',methods=['POST'])
def school2(id):
  username = request.cookies.get('login')
  if username==None:
    return redirect('/')
  listy=[]
  with open('static/schools.txt') as listy:
    listy=listy.readlines()
  id=int(id)
  id=id-1
  school=listy[id]
  id=id+1
  id=str(id)
  with open("static/json/schoollogs.json",'r') as file:
    file=json.load(file)
  file.append([username,id])
  with open("static/json/schoollogs.json",'w') as out:
    json.dump(file,out,indent=4)
  return 'Yay done!'


@app.route('/')
def main():
  #if 'testpreparer' not in request.url_root:
    #return redirect('https://testpreparer.gq')
  username = request.cookies.get('login')
  if username==None:
    not_logged_in=True
  else:
    not_logged_in=False
  return render_template('home.html',token=not_logged_in)


@app.route('/login')
def login():
  username = request.cookies.get('login')
  if username!=None:
    return redirect('/')
  return render_template('index.html')


@app.route('/login',methods=['POST'])
def main1():
  import hashlib
  name=request.form['email']
  
  psw=request.form['password']
  psw=hashlib.md5(bytes(psw, 'utf-8'))
  psw=(psw.hexdigest())
  with open('static/json/members.json','r') as file:
      var=json.load(file)
  not_found=True
  for i in range(0,len(var)):
    if var[i]["email"]==name:
      value=i
      not_found=False
      break
  if not_found==True:
    return render_template('index.html',name=name,psw=psw,error='Please create your account using the Sign Up button below!')
  else:
    if var[value]["password"]==psw:
      resp = make_response(redirect('/'))
      resp.set_cookie('login', name)
      resp.set_cookie('psw', psw)
      return resp 
    else:
      return render_template('index.html',name=name,psw=psw,error='Wrong Password!!!')
  return redirect('/')


@app.route('/signup')
def signup():
  username = request.cookies.get('login')
  if username!=None:
    return redirect('/')
  return render_template('signup.html')


@app.route('/signup',methods=['POST'])
def signup1():
  
  import hashlib
  username=request.form['username']
  first=request.form['fn']
  last=request.form['ln']
  email=request.form['email']
  check=request.form['check']
  psw=request.form['password']
  psw=hashlib.md5(bytes(psw, 'utf-8'))
  psw=(psw.hexdigest())
  psw1=request.form['confirm_password']
  psw1=hashlib.md5(bytes(psw1, 'utf-8'))
  psw1=(psw1.hexdigest())
  confirm=(psw==psw1)
  if confirm==False:
    return render_template('signup.html',error='Two passwords do not match!!!',username=username,first=first,last=last,email=email,psw=psw,psw1=psw1)
  else:
    temp={"username":username,"first":first,"last":last,"email":email,"password":psw}
    with open('static/json/members.json','r') as file:
      var=json.load(file)
    for i in range(0,len(var)):
      if var[i]["username"]==username:
        return render_template('signup.html',error='Username Exists!',username=username,first=first,last=last,email=email,psw=psw,psw1=psw1)
      if var[i]["email"]==username:
        return render_template('signup.html',error='Email Exists!',username=username,first=first,last=last,email=email,psw=psw,psw1=psw1)
    var.append(temp)
    with open('static/json/members.json','w') as file:
      var=json.dump(var, file,indent=4)
    if check=='no':
      return redirect('/login')
    resp = make_response(redirect(check))
    resp.set_cookie('login', email)
    resp.set_cookie('psw', psw)
    return resp
@app.route('/zoom')
def zoom():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  username = request.cookies.get('login')
  if username==None:
    return render_template('index.html')
  return render_template('zoom.html')
@app.route('/zoom',methods=['POST'])
def join():
  id=request.form['id']
  pwd=request.form['pwd']
  return redirect(f'zoommtg://zoom.us/join?confno={id}&pwd={pwd}')
@app.route('/launch')
def launch():
  return render_template('app.html')
@app.route('/app')
def courses():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')

  with open('static/json/courses.json') as file:
    f=json.load(file)
  new=[]
  for i in range(0,len(f)):
    if f[i][3].strip()==username.strip():
      new.append(f[i])
  ans=[]
  for i in range(0,len(new)):
    link='course/2021'+str(f.index(new[i]))+'#'
    ans.append([new[i][0].strip(),new[i][1].strip(),new[i][2].strip(),link])

  return render_template('courses.html',new=ans)
  
@app.route('/add-course')
def addcourse():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  return render_template('add.html')
@app.route('/add-course',methods=['POST'])
def addcourse1():
  username = request.cookies.get('login')
  name=request.form['name']
  image=request.form['image']
  teacher=request.form['title']+request.form['last']
  with open('static/json/courses.json') as file:
    file=json.load(file)
  file.append([name,image,teacher,username])
  with open('static/json/courses.json','w') as out:
    file=json.dump(file,out,indent=4)
  return render_template('add.html',entered=True, name=name, image=image, teacher=teacher)
@app.route('/addquiz')
def addquiz():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  with open('static/json/courses.json') as file:
    f=json.load(file)
  new=[]
  for i in range(0,len(f)):
    if f[i][3].strip()==username.strip():
      new.append(f[i])
  ans=[]
  for i in range(0,len(new)):
    link='course/2021'+str(i)+'#'
    ans.append([new[i][0].strip(),new[i][1].strip(),new[i][2].strip(),link])
  return render_template('addquiz.html',new=ans)
@app.route('/addquiz',methods=['POST'])
def addquizmethod():
  name=request.form['name']
  datey=request.form['date']
  typey=request.form['type']
  course=request.form['course']
  with open('static/json/quiz.json','r') as read:
    read=json.load(read)
  read.append({'name':name,'date':datey,'type':typey,'course':course})
  with open('static/json/quiz.json','w') as out:
    read=json.dump(read,out,indent=4)
  return redirect('/addquiz')
@app.route('/course/<course>')
def course(course):
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  username = request.cookies.get('login')
  from os import walk

  with open('static/json/courses.json') as file:
    f = json.load(file)
  course=course[4:len(course)]
  course=int(course)
  try:
    a=f[course]
  except ValueError:
    return 'Invalid Course'
  number=int(course)
  data=f[number]
  if data[3].strip()!=username:
    return 'unauthorized!'
  with open('static/json/courses.json') as file:
    f=json.load(file)
  data=f[course]
  name=data[0]
  image=data[1]
  teacher=data[2]
  
  cw=[['/edit','Edit the files here. (Click Me)','gdrive.svg']]
  hw=[['/edit','Edit the files here. (Click Me)','gdrive.svg']]
  notes=[['/edit','Edit the files here. (Click Me)','gdrive.svg']]
  sg=[['/edit','Edit the files here. (Click Me)','gdrive.svg']]
  qz=[['/edit','Edit the files here. (Click Me)','quizlet.png']]
  ws=[['/edit','Edit the files here. (Click Me)','gdrive.svg']]
  
  with open("static/json/main.json") as read_file:
    data = json.load(read_file)
  
  for i in range(0,len(data)):
    temp=dict(data[i])
    if int(temp["course"])==number:
      if temp["category"]=="notes":
        notes.append([temp["url"],temp["name"],temp["type"]])
      if temp["category"]=="sg":
        sg.append([temp["url"],temp["name"],temp["type"]])
      if temp["category"]=="hw":
        hw.append([temp["url"],temp["name"],temp["type"]])
      if temp["category"]=="cw":
        cw.append([temp["url"],temp["name"],temp["type"]])
      if temp["category"]=="ws":
        ws.append([temp["url"],temp["name"],temp["type"]])
      if temp["category"]=="qz":
        qz.append([temp["url"],temp["name"],temp["type"]])
  
  with open('static/json/quiz.json','r') as read:
    quiz=json.load(read)
    quiz=[{"name":"Quizzes are listed Below","type":"INFORMATION","date":" "}]
  return render_template('mycourse.html',course=course,name=name,image=image,teacher=teacher,notes=notes,hw=hw,cw=cw,sg=sg,quiz=quiz,ws=ws,qz=qz)
@app.route('/music')
def music():
    username = request.cookies.get('login')
    if username==None:
      return redirect('/login')
    return render_template('music.html')

@app.route('/music',methods=['POST'])
def new():
    text = request.form['search']
    processed_text = text.upper()
    import urllib.request
    import re
    search_keyword=processed_text
    while ' ' in search_keyword:
      for i in range(0,len(search_keyword)):
        if ' '==search_keyword[i]:
          search_keyword=search_keyword[0:i]+'%20'+search_keyword[i+1:len(search_keyword)]
          break
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    if len(video_ids)==0:
      return render_template('musicresults.html',noresults=True)
    else:
      mylist=[]
      for i in range(0,len(video_ids)):
        if i<10:
          mylist.append(video_ids[i])
        else:
          break
    return render_template('musicresults.html',noresults=False,mylist=mylist)
@app.route('/spotify')
def main_():
    #return "Your bot is alive!"
    return """
    <style>
    /* Style the search box inside the navigation bar */
    body{
      background-image:url('/static/bkg.png');
    }
    .search {
      padding: 20px 10px 20px 10px;
      border: none;
      margin-top: 8px;
      margin-right: 10px;
      font-size: 17px;
      position: absolute;         
      top: 50%;        
      transform: translate(0, -50%) }
    .submit {
      padding: 20px 10px 20px 10px;
      color:white;
      background-image:linear-gradient(to bottom right,#8B88E9,#A188EA,#B586EB,#CB86EB);
      margin-top: 8px;
      margin-right: 16px;
      font-size: 17px;
      position: absolute;         
      top: 70%;  
      border-radius:10px;      
      transform: translate(0, -50%) }
    }
    </style>
    <body>
    <center>
    <form  method="POST">
    <input type="text" placeholder="Search.." class='search' name='search'>
    <input type="submit" class="submit">
    </form>
    </center>
    </body>"""

@app.route('/spotify',methods=['POST'])
def new_():
    client_id = '530f3ee5ec4e4ac19c4bfdd733524928'
    client_secret = 'eb7d066e09c84921ad3ee05723fda137'
    text = request.form['search']
    processed_text = text
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    birdy_uri = 'spotify:artist:'+processed_text
    #spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
      results = spotify.next(results)
      albums.extend(results['items'])
    aaa=''
    for album in albums:
        aaa+=(album['name'])
    return aaa+'<iframe src="https://open.spotify.com/embed/track/6CR8JUW0AOPTGhCrz0P6dC" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
@app.route('/play/<id_>')
def add(id_:str):
  #import gdata.youtube
  #i#mport gdata.youtube.service

  #yt_service = gdata.youtube.service.YouTubeService()
  m="""
  <meta property="og:type" content="article">3
       <meta property="og:url" content="https://apollo.nicholasxwang.repl.co/">
       <meta property="fb:app_id" content="217926898242066">
       <meta property="og:video" content='https://www.youtube.com/watch?v="""+id_+"""'/>
       <meta property="og:video:width" content="640" />
       <meta property="og:video:height" content="426" />
       <meta property="og:video:type" content="application/mp4" />
       <meta property="og:video" content='https://www.youtube.com/watch?v="""+id_+"""'/>
       <meta property="og:video:type" content="video/mp4" />
       <meta property="og:video" content='https://www.youtube.com/watch?v="""+id_+"""'/>
       <meta property="og:video:type" content="text/html" />
       <meta property="og:title" content="title text">
       <meta property="og:image" content="https://static.thenounproject.com/png/2577569-200.png"/>
       <meta property="og:description"  content="description text"/>
       <meta property="og:site_name" content="🎵 Apollo 🎵">
"""
  a='<style>body{background:black;}</style><iframe width="100%" height="100%" src="https://www.youtube.com/embed/'+id_+'?autoplay=1&loop=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'+m
  return a
@app.route('/calendar')
def calendar():
  return render_template('calendar.html')
@app.route('/search')
def search():
    #return "Your bot is alive!"
    return """
    <style>
    /* Style the search box inside the navigation bar */
    body{
      background-color:#2f3438;
      color:white;
    }
    .search {
      width:75%;
      height:5%;
      border: none;
      font-size: 17px;
      border-radius:10px;
}
    .submit {
      width:20%;
      height:5%;
      color:white;
      background-image:linear-gradient(to bottom right,#8B88E9,#A188EA,#B586EB,#CB86EB);
      font-size: 17px;      
      border-radius:10px;
      border-style:none;      
 }
    </style>
    <body>
    <center>
    <form  method="POST">
    <input type="text" placeholder="Search.." class='search' name='search'>
    <input type="submit" class="submit">
    </form>
    <h1>When you search, results appear here!</h1>
    </center>
    </body>"""

@app.route('/search',methods=['POST'])
def search2():
    text = request.form['search']
    processed_text = text.upper()
    import urllib.request
    import re
    search_keyword=processed_text
    while ' ' in search_keyword:
      for i in range(0,len(search_keyword)):
        if ' '==search_keyword[i]:
          search_keyword=search_keyword[0:i]+'%20'+search_keyword[i+1:len(search_keyword)]
          break
    html = urllib.request.urlopen("https://www.google.com/search?q=" + search_keyword+"&safe=strict")
    video_ids = re.findall("/", html.read().decode())
    return str(html)
    """
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    return ('<iframe width="560" height="315" src="https://www.youtube.com/embed/'+video_ids[0]+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    """
    string="""<script>
    if (document.addEventListener) {
  document.addEventListener('contextmenu', function(e) {
    alert("You've tried to open context menu"); //here you draw your own menu
    e.preventDefault();
  }, false);
} else {
  document.attachEvent('oncontextmenu', function() {
    alert("You've tried to open context menu");
    window.event.returnValue = false;
  });
}
</script>
    <style>
    /* Style the search box inside the navigation bar */
    body{
      background-color:#2f3438;
      color:white;
    }
    .search {
      width:75%;
      height:5%;
      border: none;
      font-size: 17px;
      border-radius:10px;
}
    .submit {
      width:20%;
      height:5%;
      color:white;
      background-image:linear-gradient(to bottom right,#8B88E9,#A188EA,#B586EB,#CB86EB);
      font-size: 17px;      
      border-radius:10px;
      border-style:none;      
 }
    </style>
    <body>
    <center>
    <form  method="POST">
    <input type="text" placeholder="Search.." class='search' name='search'>
    <input type="submit" class="submit">
    </form>
    """
    if len(video_ids)==0:
      return 'No Results :('
    else:
      for i in range(0,len(video_ids)):
        if i<10:
          string+=('<iframe width="560" height="315" src="https://www.youtube.com/embed/'+video_ids[i]+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br><br>')
        else:
          break
    return string
    

@app.route('/share')
def shareerror():
  return redirect('/shared')
@app.route('/shared')
def share():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  with open('static/json/share.json','r') as share:
    share=json.load(share)
  new=[]
  for i in range(0,len(share)):
    if username in list(share[i]["shared"]):
      myname=share[i]["name"]
      if len(myname)>8:
        myname=myname[0:5]+'...'
      new.append({
        "name": myname,
        "name2":share[i]["name"],
        "type": share[i]["type"],
        "category": share[i]["category"],
        "user": share[i]["user"],
        "share": share[i]["share"],
        "link": share[i]["link"]
    })
  return render_template('sharedash.html',new=new)
@app.route('/shared/new')
def shared():
  username = request.cookies.get('login')
  if username==None:
    return redirect('/login')
  with open('static/json/members.json','r') as members:
    members=json.load(members)
  return render_template('share.html',members=members)
@app.route('/shared/file/<file>')
def openfile(file):
  with open("static/json/share.json", "r") as read_file:
    data = json.load(read_file)
  for i in range(0,len(data)):
    if file==data[i]["link"]:
      return redirect(data[i]["url"])
  return 'We could not find your file!'
    
@app.route('/shared/new',methods=['POST'])
def share1():
  members=request.form.getlist('members')
  share=request.form['share']
  category=request.form['category']
  typey=request.form['type']
  name=request.form['name']
  url=request.form['url']
  myname=request.cookies.get('login')
  digits=['a','b','c','d','e','f','g','h','i','j','k','l','m','n' 'o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'NO', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z','1','2','3','4','5','6','7','8','9','0']
  link=''
  import random
  for i in range(0,30):
    link+=random.choice(digits)
  with open("static/json/share.json", "r") as read_file:
    data = json.load(read_file)
  data.append({"name":name,
    "url":url,
    "type":typey,
    "shared":members,
    "category":category,
    "user":myname,
    "share":share,
    "link":link})
  with open("static/json/share.json", "w") as write_file:
    json.dump(data, write_file,indent=4)
  link='https://testpreparer.gq/shared/file/'+link
  msg = Message('New Document from '+myname, sender = 'testpreparergq@gmail.com', recipients = list(members))
  msg.html = """<h1>New Document Shared with You</h1>
  <p>Hi, """+myname+""" shared with you the document: 
  """+name+"""! Please open your file in this link: """+link
  mail.send(msg)
  return 'Success'
if __name__ == '__main__':
	app.run(host = "0.0.0.0", port = 0000)