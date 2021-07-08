from flask import Flask, render_template, request, make_response, redirect, flash, url_for
import requests
import hashlib
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)
import json
import os
import random
from werkzeug.security import generate_password_hash, check_password_hash

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testpreparergq@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('psw')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

import community
import account
import extentions


@app.route('/testing/<file>')
def fil2(file):
    return render_template(file)


@app.route('/partners/cbot/redeem')
def cbot_premium():
    import json
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    login = True
    if username == None:
        login = False
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                login = False
            else:
                found = True
    if found == False:
        login = False

    from urllib.request import urlopen
    import json
    url = "https://cbotdiscord.npcool.repl.co/static/main.json"
    response = urlopen(url)
    data_json = json.loads(response.read())

    try:
        data_json[username]
    except:
        return render_template('c_premium.html',
                               login=login,
                               username=username)
    return 'You have claimed premium!'


@app.route('/try', methods=['POST'])
def tryit():

    code = request.form['mycode']
    import io
    import contextlib
    import sys

    stdout = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout):
            exec(code)

            result = f"{stdout.getvalue()}"
    except Exception as e:
        result = f"<span  style='color:#ed004b;'>{type(e).__name__}:  {e.args}</span>"

    return "<style>body{background:black;color:white;font-family:'Arial';}h1{background:#363636;border-radius:10px;padding:5px;width:150px;}</style><h1>Console</h1>" "" + result


@app.route('/python')
def python():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('python.html')


@app.errorhandler(404)
def page_not_found(e):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found1(e):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('500.html'), 500


@app.errorhandler(400)
def page_not_found2(e):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('400.html'), 400


@app.route('/question')
def question():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('question.html')


@app.route('/question', methods=['POST'])
def question2():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    query = request.form['text']
    from pprint import pprint
    import requests
    import os
    import urllib.parse

    appid = os.getenv('WA_APPID')

    query = urllib.parse.quote_plus("lifespan of a mosquito")
    query_url = f"http://api.wolframalpha.com/v2/query?" \
          f"appid={appid}" \
          f"&input={query}" \
          f"&format=plaintext" \
          f"&output=json"

    r = requests.get(query_url).json()

    data = r["queryresult"]["pods"][0]["subpods"][0]
    datasource = ", ".join(data["datasources"]["datasource"])
    microsource = data["microsources"]["microsource"]
    plaintext = data["plaintext"]

    return (f"Result: '{plaintext}' from {datasource} ({microsource}).")
    # Result: '(9.2 to 11, 52 to 60) days' from AmazingNumbers, TheWikimediaFoundationIncWikipedia (SpeciesData).


@app.route('/cookies')
def cookies():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('cookies.html')


@app.route('/pp')
def pp():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('pp.html')


@app.route('/about')
def about():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('about.html')


@app.route('/aops')
def aops():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('aops.html')


@app.route('/discord')
def disc():
    return redirect('https://discord.gg/Ac35ApunJY')


@app.route('/disclaimer')
def disclaimer():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('disclaimer.html')


@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('login', '', expires=0)
    return resp


@app.route('/tos')
def tos():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('tos.html')


@app.route('/static/json/<file>')
def protect(file):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('404.html')


@app.route('/edit')
def edit():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')

    from os import walk

    with open('static/json/courses.json') as file:
        f = json.load(file)
    new = []
    for i in range(0, len(f)):
        if f[i][3].strip() == username.strip():
            new.append([f[i][0], str(i)])
    return render_template('edit.html', new=new)


@app.route('/edit', methods=['POST'])
def edit2():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    from os import walk

    with open('static/json/courses.json') as file:
        f = json.load(file)
    new = []
    for i in range(0, len(f)):
        if f[i][3].strip() == username.strip():
            new.append([f[i][0], str(i)])
    with open("static/json/main.json", "r") as read_file:
        data = json.load(read_file)
    name = request.form['name']
    url = request.form['url']
    type1 = request.form['type']
    course = request.form['course']
    category = request.form['category']

    user = request.cookies.get('login')
    data.append({
        "name": name,
        "url": url,
        "type": type1,
        "course": course,
        "category": category,
        "user": user
    })
    with open("static/json/main.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
    return render_template('edit.html',
                           entered=True,
                           url=url,
                           type=type1,
                           course=course,
                           category=category,
                           name=name,
                           new=new)


@app.route('/school/<id>')
def school1(id):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    listy = []
    with open('static/schools.txt') as listy:
        listy = listy.readlines()
    id = int(id)
    id = id - 1
    school = listy[id]
    id = id + 1
    id = str(id)
    return render_template('myschool.html', school=school, id=id)


@app.route('/school/<id>', methods=['POST'])
def school2(id):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    listy = []
    with open('static/schools.txt') as listy:
        listy = listy.readlines()
    id = int(id)
    id = id - 1
    school = listy[id]
    id = id + 1
    id = str(id)
    with open("static/json/schoollogs.json", 'r') as file:
        file = json.load(file)
    file.append([username, id])
    with open("static/json/schoollogs.json", 'w') as out:
        json.dump(file, out, indent=4)
    return 'Yay done!'


@app.route('/')
def main():
    username = request.cookies.get('login')
    login = True
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        login = False
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                login = False
            else:
                found = True
    if found == False:
        login = False
    return render_template('home.html', token=not login)


@app.route('/login')
def login():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if 'login' in request.args.get('path'):
        return redirect('/login?path=/')

    signup = '/signup?path=' + request.args.get('path')
    if username == None:
        return render_template('login.html', signup=signup)
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
        return render_template('login.html', signup=signup)
    return redirect('/')


@app.route('/login', methods=['POST'])
def main1():
    name = request.form['email']

    psw = request.form['password']
    psw = hashlib.md5(bytes(psw, 'utf-8'))
    psw = (psw.hexdigest())
    with open('static/json/members.json', 'r') as file:
        var = json.load(file)
    not_found = True
    for i in range(0, len(var)):
        if var[i]["email"] == name:
            value = i
            not_found = False
            break
    if not_found == True:
        return render_template(
            'login.html',
            name=name,
            psw=psw,
            error='Please create your account using the Sign Up button below!')
    else:
        if var[value]["password"] == psw:
            resp = make_response(
                redirect('https://testpreparer.gq' + request.args.get('path')))
            resp.set_cookie('login', name)
            resp.set_cookie('psw', str(psw))
            return resp
        else:
            return render_template('login.html',
                                   name=name,
                                   psw=psw,
                                   error='Wrong Password!!!')
    return redirect('/')


@app.route('/signup')
def signup():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return render_template('signup.html')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return render_template('signup.html')
            else:
                found = True
    if found == False:
        return render_template('signup.html')
    return redirect('/')


@app.route('/signup', methods=['POST'])
def signup1():

    import hashlib
    username = request.form['username']
    first = request.form['fn']
    last = request.form['ln']
    email = request.form['email']
    check = request.form['check']
    psw = request.form['password']
    psw = hashlib.md5(bytes(psw, 'utf-8'))
    psw = (psw.hexdigest())
    psw1 = request.form['confirm_password']
    psw1 = hashlib.md5(bytes(psw1, 'utf-8'))
    psw1 = (psw1.hexdigest())
    confirm = (psw == psw1)
    if confirm == False:
        return render_template('signup.html',
                               error='Two passwords do not match!!!',
                               username=username,
                               first=first,
                               last=last,
                               email=email,
                               psw=psw,
                               psw1=psw1)
    else:
        temp = {
            "username": username,
            "first": first,
            "last": last,
            "email": email,
            "password": psw
        }
        with open('static/json/members.json', 'r') as file:
            var = json.load(file)
        for i in range(0, len(var)):
            if var[i]["username"] == username:
                return render_template('signup.html',
                                       error='Username Exists!',
                                       username=username,
                                       first=first,
                                       last=last,
                                       email=email,
                                       psw=psw,
                                       psw1=psw1)
            if var[i]["email"] == username:
                return render_template('signup.html',
                                       error='Email Exists!',
                                       username=username,
                                       first=first,
                                       last=last,
                                       email=email,
                                       psw=psw,
                                       psw1=psw1)
        var.append(temp)
        with open('static/json/members.json', 'w') as file:
            var = json.dump(var, file, indent=4)
        resp = make_response(
            redirect('https://testpreparer.gq' + request.args.get('path')))
        resp.set_cookie('login', email)
        resp.set_cookie('psw', psw)
        return resp


@app.route('/zoom')
def zoom():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('zoom.html')


@app.route('/zoom', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    return redirect(f'zoommtg://zoom.us/join?confno={id}&pwd={pwd}')


@app.route('/launch')
def launch():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('app.html')


@app.route('/app')
def mainlol():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('dashboard.html')


@app.route('/education')
def courses():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')

    with open('static/json/courses.json') as file:
        f = json.load(file)
    new = []
    for i in range(0, len(f)):
        if f[i][3].strip() == username.strip():
            new.append(f[i])
    ans = []
    for i in range(0, len(new)):
        link = 'course/2021' + str(f.index(new[i])) + '#'
        ans.append(
            [new[i][0].strip(), new[i][1].strip(), new[i][2].strip(), link])

    return render_template('courses.html', new=ans)


@app.route('/add-course')
def addcourse():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('add.html')


@app.route('/add-course', methods=['POST'])
def addcourse1():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    username = request.cookies.get('login')
    name = request.form['name']
    image = request.form['image']
    teacher = request.form['title'] + request.form['last']
    with open('static/json/courses.json') as file:
        file = json.load(file)
    file.append([name, image, teacher, username])
    with open('static/json/courses.json', 'w') as out:
        file = json.dump(file, out, indent=4)
    return render_template('add.html',
                           entered=True,
                           name=name,
                           image=image,
                           teacher=teacher)


@app.route('/addquiz')
def addquiz():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/courses.json') as file:
        f = json.load(file)
    new = []
    for i in range(0, len(f)):
        if f[i][3].strip() == username.strip():
            new.append(f[i])
    ans = []
    for i in range(0, len(new)):
        link = 'course/2021' + str(i) + '#'
        ans.append(
            [new[i][0].strip(), new[i][1].strip(), new[i][2].strip(), link])
    return render_template('addquiz.html', new=ans)


@app.route('/addquiz', methods=['POST'])
def addquizmethod():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    name = request.form['name']
    datey = request.form['date']
    typey = request.form['type']
    course = request.form['course']
    with open('static/json/quiz.json', 'r') as read:
        read = json.load(read)
    read.append({'name': name, 'date': datey, 'type': typey, 'course': course})
    with open('static/json/quiz.json', 'w') as out:
        read = json.dump(read, out, indent=4)
    return redirect('/addquiz')


@app.route('/course/<course>')
def course(course):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    from os import walk

    with open('static/json/courses.json') as file:
        f = json.load(file)
    course = course[4:len(course)]
    course = int(course)
    try:
        a = f[course]
    except ValueError:
        return 'Invalid Course'
    number = int(course)
    data = f[number]
    if data[3].strip() != username:
        return 'unauthorized!'
    with open('static/json/courses.json') as file:
        f = json.load(file)
    data = f[course]
    name = data[0]
    image = data[1]
    teacher = data[2]

    cw = [['/edit', 'Edit the files here. (Click Me)', 'gdrive.svg']]
    hw = [['/edit', 'Edit the files here. (Click Me)', 'gdrive.svg']]
    notes = [['/edit', 'Edit the files here. (Click Me)', 'gdrive.svg']]
    sg = [['/edit', 'Edit the files here. (Click Me)', 'gdrive.svg']]
    qz = [['/edit', 'Edit the files here. (Click Me)', 'quizlet.png']]
    ws = [['/edit', 'Edit the files here. (Click Me)', 'gdrive.svg']]

    with open("static/json/main.json") as read_file:
        data = json.load(read_file)

    for i in range(0, len(data)):
        temp = dict(data[i])
        if int(temp["course"]) == number:
            if temp["category"] == "notes":
                notes.append([temp["url"], temp["name"], temp["type"]])
            if temp["category"] == "sg":
                sg.append([temp["url"], temp["name"], temp["type"]])
            if temp["category"] == "hw":
                hw.append([temp["url"], temp["name"], temp["type"]])
            if temp["category"] == "cw":
                cw.append([temp["url"], temp["name"], temp["type"]])
            if temp["category"] == "ws":
                ws.append([temp["url"], temp["name"], temp["type"]])
            if temp["category"] == "qz":
                qz.append([temp["url"], temp["name"], temp["type"]])

    with open('static/json/quiz.json', 'r') as read:
        quiz = json.load(read)
        quiz = [{
            "name": "Quizzes are listed Below",
            "type": "INFORMATION",
            "date": " "
        }]
    return render_template('mycourse.html',
                           course=course,
                           name=name,
                           image=image,
                           teacher=teacher,
                           notes=notes,
                           hw=hw,
                           cw=cw,
                           sg=sg,
                           quiz=quiz,
                           ws=ws,
                           qz=qz)


@app.route('/music')
def music():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('music.html')


@app.route('/music', methods=['POST'])
def new():

    text = request.form['search']
    import requests

    CLIENT_ID = '2e2775cd017f44a8a3e61d769f157732'
    CLIENT_SECRET = '532893224edb4486ab23aa4bccbc95fc'
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    # POST
    auth_response = requests.post(
        AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    artist_info = requests.get(
        f'https://api.spotify.com/v1/search?q={text}&type=track',
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }).json()
    #print(artist_info)
    print(access_token)

    spotify_arr = []
    with open('static/json/cache.json', 'r') as file:
        file = json.load(file)
    for i in range(0, len(artist_info['tracks']['items'])):
        if i < 10:
            mydict = {}
            mydict['image'] = str(
                artist_info['tracks']['items'][i]['album']['images'][0]['url'])
            mydict['author'] = (artist_info['tracks']['items'][i]['album']
                                ['artists'][0]['name'])
            mydict['author_url'] = artist_info['tracks']['items'][i]['album'][
                'artists'][0]['external_urls']["spotify"]
            mydict['album'] = (
                artist_info['tracks']['items'][i]['album']['name'])
            mydict['explicit'] = artist_info['tracks']['items'][i]['explicit']
            mydict['name'] = (artist_info['tracks']['items'][i]['name'])
            mydict['preview'] = (
                artist_info['tracks']['items'][i]['preview_url'])
            mydict['link'] = (
                artist_info['tracks']['items'][i]['external_urls']['spotify'])
            mydict['code'] = mydict['link'][31:len(mydict['link'])]
            mydict['uri'] = (artist_info['tracks']['items'][i]['uri'])
            spotify_arr.insert(0, mydict)
            file.append(mydict)
    processed_text = text.upper()
    with open('static/json/cache.json', 'w') as out:
        file = json.dump(file, out, indent=4)
    import urllib.request
    import re
    search_keyword = processed_text
    while ' ' in search_keyword:
        for i in range(0, len(search_keyword)):
            if ' ' == search_keyword[i]:
                search_keyword = search_keyword[0:i] + '%20' + search_keyword[
                    i + 1:len(search_keyword)]
                break
    
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query=" + search_keyword)

    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    def find_data(link, param):
        #author_name
        #author_url
        #thumbnail_url
        #title
        import urllib.request
        import json
        import urllib
        import pprint

        #change to yours VideoID or change url inparams
        VideoID = link

        params = {
            "format": "json",
            "url": "https://www.youtube.com/watch?v={}".format(VideoID)
        }
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            #pprint.pprint(data)
            return data[param]

    if len(video_ids) == 0 and len(spotify_arr) == 0:
        return render_template('musicresults.html', noresults=True)

    else:
        mylist = []
        for i in range(0, len(video_ids)):
            if i < 10:
                #author_name
                #author_url
                #thumbnail_url
                #title

                try:
                  my_dict = {"id": video_ids[i]}
                  my_dict["author_name"] = find_data(video_ids[i], "author_name")
                  my_dict["author_url"] = find_data(video_ids[i], "author_url")
                  my_dict["thumbnail_url"] = find_data(video_ids[i],"thumbnail_url")
                  my_dict["title"] = find_data(video_ids[i], "title")
                  mylist.append(my_dict)
                except:
                  continue
              
            else:
                break

    return render_template('musicresults.html',
                           noresults=False,
                           mylist=mylist,
                           spotify_arr=spotify_arr)


@app.route('/play/spotify/<smth>')
def spotify(smth):
    extra = ''
    with open('static/json/cache.json', 'r') as file:
        file = json.load(file)
    for i in file:
        if i['code'] == smth:
            return render_template('musictrack.html', i=i)


@app.route('/play/<id_>')
def add(id_:str):
  def find_data(link, param):
      #author_name
      #author_url
      #thumbnail_url
      #title
      import urllib.request
      import json
      import urllib
      import pprint
      #change to yours VideoID or change url inparams
      VideoID = link
      params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
      url = "https://www.youtube.com/oembed"
      query_string = urllib.parse.urlencode(params)
      url = url + "?" + query_string
      with urllib.request.urlopen(url) as response:
          response_text = response.read()
          data = json.loads(response_text.decode())
          pprint.pprint(data)
          return data[param]
  
  youtube = f'https://www.youtube.com/watch?v={id_}'
  link = f'https://testpreparer.gq/play/{id_}'
  author = find_data(id_,'author_name')
  author_url = find_data(id_,'author_url')
  sub = author_url+'?sub_confirmation=1'
  thumbnail_url = find_data(id_,'thumbnail_url')
  title = find_data(id_,'title')
  content = f'Listen to {title} by {author} on TestPreparer!'
  return render_template('musicvideo.html',author=author,author_url=author_url,thumbnail_url=thumbnail_url,title=title,id=id_,content=content,youtube=youtube,sub=sub,link=link)



@app.route('/calendar')
def calendar():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    return render_template('calendar.html')


@app.route('/shared')
def share():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/share.json', 'r') as share:
        share = json.load(share)
    new = []
    for i in range(0, len(share)):
        if username in list(share[i]["shared"]):
            myname = share[i]["name"]
            if len(myname) > 8:
                myname = myname[0:5] + '...'
            new.append({
                "name": myname,
                "name2": share[i]["name"],
                "type": share[i]["type"],
                "category": share[i]["category"],
                "user": share[i]["user"],
                "share": share[i]["share"],
                "link": share[i]["link"]
            })
    return render_template('sharedash.html', new=new)


@app.route('/shared/new')
def shared():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json', 'r') as members:
        members = json.load(members)
    return render_template('share.html', members=members)


@app.route('/shared/file/<file>')
def openfile(file):
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open("static/json/share.json", "r") as read_file:
        data = json.load(read_file)
    for i in range(0, len(data)):
        if file == data[i]["link"]:
            return redirect(data[i]["url"])
    return 'We could not find your file!'


@app.route('/shared/new', methods=['POST'])
def share1():
    username = request.cookies.get('login')
    psw = request.cookies.get('psw')
    if username == None:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    with open('static/json/members.json') as a:
        a = json.load(a)
    found = False
    for i in a:
        if i["email"] == username:
            if str(i["password"]) != str(psw):
                return redirect(
                    f'/login?path={request.path.replace("/","%2F")}')
            else:
                found = True
    if found == False:
        return redirect(f'/login?path={request.path.replace("/","%2F")}')
    members = request.form.getlist('members')
    share = request.form['share']
    category = request.form['category']
    typey = request.form['type']
    name = request.form['name']
    url = request.form['url']
    myname = request.cookies.get('login')
    digits = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'NO', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', '0'
    ]
    link = ''
    import random
    for i in range(0, 30):
        link += random.choice(digits)
    with open("static/json/share.json", "r") as read_file:
        data = json.load(read_file)
    data.append({
        "name": name,
        "url": url,
        "type": typey,
        "shared": members,
        "category": category,
        "user": myname,
        "share": share,
        "link": link
    })
    with open("static/json/share.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
    link = 'https://testpreparer.gq/shared/file/' + link
    msg = Message('New Document from ' + myname,
                  sender='testpreparergq@gmail.com',
                  recipients=list(members))
    msg.html = """<h1>New Document Shared with You</h1>
  <p>Hi, """ + myname + """ shared with you the document: 
  """ + name + """! Please open your file in this link: """ + link
    mail.send(msg)
    return 'Success'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=0000)
