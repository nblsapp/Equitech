from __main__ import app
@app.route('/logout')
def logout():
  resp = make_response(redirect('/'))
  resp.set_cookie('login', '', expires=0)
  return resp
